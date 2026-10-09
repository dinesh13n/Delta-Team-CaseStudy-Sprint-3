#Requires -Version 5.1
<#
.SYNOPSIS
    Windows / PowerShell equivalent of the Makefile.
    Targets are the transformation gates (docs/14-transformation/transformation-gates.md).
 
.DESCRIPTION
    Run one or more targets in order. Execution stops at the first failing command,
    just like make.
 
    Overrides (same names as the Makefile variables, set as environment variables):
        $env:VENV              default: .venv
        $env:BOOTSTRAP_PYTHON  default: py -3.11
        $env:PYTHON            default: <VENV>\Scripts\python.exe
        $env:SEMANTIC          default: ..\semantic-layer
        $env:ROLE              default: dispatcher (persona for the 'token' target)

.EXAMPLE
    .\make.ps1 install
.EXAMPLE
    .\make.ps1 lint test
.EXAMPLE
    $env:SEMANTIC = 'C:\src\semantic-layer'; .\make.ps1 gates
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
    [string[]] $Target = @('help')
)
 
$ErrorActionPreference = 'Stop'
 
# ---------------------------------------------------------------------------
# Variables (mirror the Makefile's ?= defaults)
# ---------------------------------------------------------------------------
$Venv            = if ($env:VENV)             { $env:VENV }                   else { '.venv' }
$BootstrapPython = if ($env:BOOTSTRAP_PYTHON) { -split $env:BOOTSTRAP_PYTHON } else { @('py', '-3.11') }
$Python          = if ($env:PYTHON)           { $env:PYTHON }                 else { Join-Path $Venv 'Scripts\python.exe' }
$Semantic        = if ($env:SEMANTIC)         { $env:SEMANTIC }               else { Join-Path '..' 'semantic-layer' }
$Role            = if ($env:ROLE)             { $env:ROLE }                   else { 'dispatcher' }
 
# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
function Invoke-Step {
    # Runs a native command, echoes it like make does, and fails on non-zero exit.
    param(
        [Parameter(Mandatory)] [string]   $Exe,
        [string[]] $Arguments = @()
    )
    Write-Host "> $Exe $($Arguments -join ' ')" -ForegroundColor DarkGray
    & $Exe @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "'$Exe $($Arguments -join ' ')' failed with exit code $LASTEXITCODE"
    }
}
 
function Invoke-Python {
    param([string[]] $Arguments)
    if (-not (Test-Path -LiteralPath $Python)) {
        throw "Virtualenv interpreter not found at '$Python'. Run '.\make.ps1 install' first."
    }
    Invoke-Step -Exe $Python -Arguments $Arguments
}
 
function Assert-Command {
    param([string] $Name, [string] $Hint)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "'$Name' was not found on PATH. $Hint"
    }
}
 
# ---------------------------------------------------------------------------
# Targets
# ---------------------------------------------------------------------------
$Tasks = [ordered]@{
 
    help = {
        Write-Host 'Usage: .\make.ps1 <target> [<target> ...]'
        Write-Host ''
        Write-Host "Targets: $(($Tasks.Keys | Where-Object { $_ -ne 'help' }) -join ', ')"
    }
 
    install = {
        $bootArgs = @($BootstrapPython | Select-Object -Skip 1) + @('-m', 'venv', $Venv)
        Invoke-Step -Exe $BootstrapPython[0] -Arguments $bootArgs
        Invoke-Python @('-m', 'pip', 'install', '--require-hashes', '-r', 'requirements-dev.txt')
    }
 
    test = {
        Invoke-Python @('-m', 'pytest', '-q')
    }
 
    cov = {
        Invoke-Python @('-m', 'pytest', '-q', '--cov', '--cov-report=term-missing',
                        '--cov-report=xml', '--junitxml=junit.xml', '--cov-fail-under=80')
    }
 
    lint = {
        Invoke-Python @('-m', 'ruff', 'check', '.')
        Invoke-Python @('-m', 'ruff', 'format', '--check', '.')
    }
 
    format = {
        Invoke-Python @('-m', 'ruff', 'format', '.')
    }
 
    type = {
        Invoke-Python @('-m', 'mypy', '--cache-dir=.mypy_cache')
    }
 
    secrets = {
        Invoke-Python @('scripts\secret_scan.py')
    }
 
    smoke = {
        Invoke-Python @('scripts\sanity_check.py')
    }
 
    etl = {
        Invoke-Python @('etl\run_daily_batch.py', '--sample')
    }
 
    rego = {
        Invoke-Python @('scripts\generate_rego.py', '--check')
        Assert-Command 'opa' 'Install it with "winget install open-policy-agent.opa" or download opa_windows_amd64.exe and add it to PATH as opa.exe.'
        Invoke-Step -Exe 'opa' -Arguments @('check', 'policy\opa')
        Invoke-Step -Exe 'opa' -Arguments @('test',  'policy\opa')
    }
 
    semantic = {
        Invoke-Python @('-m', 'pytest', '-q', (Join-Path $Semantic 'tests'))
    }
 
    characterization = {
        Invoke-Python @('-m', 'pytest', '-q', 'tests\characterization')
    }
 
    gates = {
        foreach ($t in 'lint', 'type', 'secrets', 'etl', 'test', 'smoke', 'semantic') {
            Invoke-Task $t
        }
    }
 
    run = {
        Invoke-Python @('-m', 'uvicorn', 'apps.api.main:app', '--reload')
    }
 
    # Local-only dev bearer token for the /ops/ view; needs AUTH_SECRET set to the server's secret.
    token = {
        Invoke-Python @('-m', 'scripts.issue_dev_token', $Role)
    }

    package = {
        Write-Host 'container recipe: Dockerfile (platform-neutral, ADR-0009)'
    }
}
 
function Invoke-Task {
    param([string] $Name)
    if (-not $Tasks.Contains($Name)) {
        throw "Unknown target '$Name'. Valid targets: $($Tasks.Keys -join ', ')"
    }
    if ($Name -ne 'help') { Write-Host "==> $Name" -ForegroundColor Cyan }
    & $Tasks[$Name]
}
 
# ---------------------------------------------------------------------------
# Entry point - always run from the repo root (where this script lives),
# matching how make resolves the relative paths above.
# ---------------------------------------------------------------------------
Push-Location -LiteralPath $PSScriptRoot
try {
    foreach ($t in $Target) { Invoke-Task $t }
}
catch {
    Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
finally {
    Pop-Location
}