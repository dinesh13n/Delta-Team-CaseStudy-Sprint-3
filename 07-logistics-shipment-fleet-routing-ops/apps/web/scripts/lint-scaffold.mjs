// Real (syntax-level) lint gate replacing `echo scaffold` (F-06). The portal is a scaffold and deferred (OQ-06), so
// this checks that every TypeScript source parses; type-level checks arrive when the Angular app is wired.
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";
import ts from "typescript";

const roots = ["src", "../../tests/playwright"];
const files = [];
const walk = (d) => {
  for (const n of readdirSync(d)) {
    const p = join(d, n);
    if (statSync(p).isDirectory()) walk(p);
    else if (p.endsWith(".ts")) files.push(p);
  }
};
roots.forEach((r) => { try { walk(r); } catch { /* optional root */ } });
let bad = 0;
for (const f of files) {
  const out = ts.transpileModule(readFileSync(f, "utf8"), { reportDiagnostics: true, fileName: f });
  for (const d of out.diagnostics ?? []) {
    bad++;
    console.error(`${f}: ${ts.flattenDiagnosticMessageText(d.messageText, "\n")}`);
  }
}
console.log(JSON.stringify({ checked: files.length, errors: bad }));
process.exit(bad ? 1 : 0);
