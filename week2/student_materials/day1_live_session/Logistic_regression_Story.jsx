import { useState } from "react";

const chickens = [
  { id: 1, cut: "Breast", weight: 2.0, thickness: 2.5, label: 1 },
  { id: 2, cut: "Drumstick", weight: 0.5, thickness: 1.0, label: 0 },
  { id: 3, cut: "Thigh", weight: 1.5, thickness: 1.5, label: 1 },
  { id: 4, cut: "Half Chicken", weight: 3.0, thickness: 3.0, label: 1 },
  { id: 5, cut: "Wing", weight: 0.75, thickness: 0.5, label: 0 },
];

const LR = 1.0;

function sigmoid(z) { return 1 / (1 + Math.exp(-z)); }
function logLoss(y, p) {
  const c = Math.max(1e-7, Math.min(1 - 1e-7, p));
  return -(y * Math.log(c) + (1 - y) * Math.log(1 - c));
}

// Pre-train all epochs so numbers are real
function buildHistory() {
  let w1 = 0.75, w2 = 0.00, b = 0.25;
  const hist = [];
  for (let ep = 0; ep <= 20; ep++) {
    let sumGW1 = 0, sumGW2 = 0, sumGB = 0, totalLoss = 0, correct = 0;
    const details = [];
    for (const c of chickens) {
      const z = w1 * c.weight + w2 * c.thickness + b;
      const yHat = sigmoid(z);
      const loss = logLoss(c.label, yHat);
      const error = yHat - c.label;
      const gw1 = error * c.weight;
      const gw2 = error * c.thickness;
      const gb = error;
      sumGW1 += gw1; sumGW2 += gw2; sumGB += gb;
      totalLoss += loss;
      if ((yHat >= 0.5 ? 1 : 0) === c.label) correct++;
      details.push({ z, yHat, loss, error, gw1, gw2, gb, correct: (yHat >= 0.5 ? 1 : 0) === c.label });
    }
    const avgGW1 = sumGW1 / 5, avgGW2 = sumGW2 / 5, avgGB = sumGB / 5;
    const avgLoss = totalLoss / 5;
    hist.push({ w1, w2, b, avgGW1, avgGW2, avgGB, avgLoss, correct, details, sumGW1, sumGW2, sumGB });
    w1 -= LR * avgGW1;
    w2 -= LR * avgGW2;
    b -= LR * avgGB;
  }
  return hist;
}
const trainingHistory = buildHistory();

function SigmoidViz({ z, yHat }) {
  const w = 100, h = 42, pad = 5;
  const pW = w - pad * 2, pH = h - pad * 2;
  const pts = [];
  for (let i = 0; i <= 40; i++) {
    const zv = -5 + (i / 40) * 10;
    pts.push(`${pad + (i / 40) * pW},${pad + (1 - sigmoid(zv)) * pH}`);
  }
  const cz = Math.max(-5, Math.min(5, z));
  const dx = pad + ((cz + 5) / 10) * pW;
  const dy = pad + (1 - yHat) * pH;
  return (
    <svg width={w} height={h} className="block">
      <polyline points={pts.join(" ")} fill="none" stroke="#94A3B8" strokeWidth="1.5" />
      <line x1={pad} y1={pad + pH / 2} x2={pad + pW} y2={pad + pH / 2} stroke="#E2E8F0" strokeWidth="0.5" strokeDasharray="3,3" />
      <circle cx={dx} cy={dy} r="3.5" fill="#0EA5E9" stroke="#fff" strokeWidth="1.5" />
    </svg>
  );
}

function Expand({ title, children }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="mt-1">
      <button onClick={() => setOpen(!open)} className="flex items-center gap-1 text-xs text-indigo-500 hover:text-indigo-700 font-medium">
        <span style={{ transform: open ? "rotate(90deg)" : "rotate(0deg)", transition: "transform 0.15s", display: "inline-block" }}>▶</span>
        {title}
      </button>
      {open && <div className="mt-1 ml-3 p-2 bg-slate-50 border border-slate-200 rounded-lg text-xs text-slate-600 font-mono leading-relaxed">{children}</div>}
    </div>
  );
}

function Arrow() {
  return (
    <div className="flex items-center mx-0.5 shrink-0">
      <svg width="20" height="12" viewBox="0 0 20 12"><path d="M0 6 L12 6 M9 2.5 L15 6 L9 9.5" stroke="#CBD5E1" strokeWidth="1.5" fill="none" /></svg>
    </div>
  );
}

function ChickenRow({ chicken, detail, weights }) {
  const { w1, w2, b } = weights;
  const { z, yHat, loss, correct } = detail;
  const lf = chicken.label === 1 ? "-log(ŷ)" : "-log(1-ŷ)";
  return (
    <div className="rounded-xl bg-white mb-2.5 border border-slate-200 overflow-hidden" style={{ boxShadow: "0 1px 2px rgba(0,0,0,0.04)" }}>
      <div className="flex items-center py-2.5 px-3">
        <div className="flex flex-col items-center min-w-20">
          <div className="text-lg">🍗</div>
          <div className="text-xs font-bold text-slate-700">{chicken.cut}</div>
          <div className="text-xs text-slate-400">{chicken.weight}lbs, {chicken.thickness}″</div>
        </div>
        <Arrow />
        <div className="flex flex-col items-center min-w-14">
          <div className="rounded-lg px-2.5 py-1.5 border-2 border-indigo-300 bg-indigo-50 text-center">
            <div className="text-xs font-bold text-indigo-400">z</div>
            <div className="text-base font-bold text-indigo-700">{z.toFixed(2)}</div>
          </div>
        </div>
        <Arrow />
        <div className="flex flex-col items-center min-w-24">
          <div className="rounded-lg px-1.5 py-1 border-2 border-sky-300 bg-sky-50 text-center">
            <div className="text-xs font-bold text-sky-400 mb-0.5">σ(z)</div>
            <SigmoidViz z={z} yHat={yHat} />
          </div>
        </div>
        <Arrow />
        <div className="flex flex-col items-center min-w-14">
          <div className="rounded-lg px-2.5 py-1.5 border-2 border-cyan-400 bg-cyan-50 text-center">
            <div className="text-xs font-bold text-cyan-500">ŷ</div>
            <div className="text-base font-bold text-cyan-700">{(yHat * 100).toFixed(1)}%</div>
          </div>
        </div>
        <Arrow />
        <div className="flex flex-col items-center min-w-10">
          <div className={`rounded-full w-8 h-8 flex items-center justify-center text-sm ${chicken.label === 1 ? "bg-emerald-500" : "bg-red-400"}`}>
            {chicken.label === 1 ? "😊" : "😞"}
          </div>
          <div className="text-xs text-slate-400">y={chicken.label}</div>
        </div>
        <Arrow />
        <div className="flex flex-col items-center min-w-16">
          <div className={`rounded-lg px-2.5 py-1.5 border-2 text-center ${loss > 0.8 ? "border-red-400 bg-red-50" : loss > 0.4 ? "border-amber-400 bg-amber-50" : "border-emerald-400 bg-emerald-50"}`}>
            <div className={`text-xs font-bold ${loss > 0.8 ? "text-red-400" : loss > 0.4 ? "text-amber-400" : "text-emerald-400"}`}>Loss</div>
            <div className="text-sm font-bold text-slate-700">{loss.toFixed(3)}</div>
            <div className="text-xs text-slate-400">{lf}</div>
          </div>
        </div>
        <div className="ml-1.5 text-base">{correct ? "✅" : "❌"}</div>
      </div>
      <div className="px-3 pb-2.5 flex gap-3 flex-wrap">
        <Expand title="z calculation">
          <div>z = ({w1.toFixed(4)} × {chicken.weight}) + ({w2.toFixed(4)} × {chicken.thickness}) + {b.toFixed(4)}</div>
          <div className="mt-1 font-bold text-indigo-600">z = {z.toFixed(4)} tsp</div>
        </Expand>
        <Expand title="σ(z) → ŷ">
          <div>σ({z.toFixed(3)}) = 1 / (1 + e<sup>-{z.toFixed(3)}</sup>) = 1 / {(1 + Math.exp(-z)).toFixed(4)}</div>
          <div className="mt-1 font-bold text-sky-600">ŷ = {yHat.toFixed(4)} → {(yHat * 100).toFixed(1)}%</div>
        </Expand>
        <Expand title="loss calculation">
          {chicken.label === 1 ? (
            <>
              <div className="font-sans text-slate-500 mb-1">y=1 → Loss = -log(ŷ) = -log({yHat.toFixed(4)})</div>
              <div className="font-bold text-amber-600">Loss = {loss.toFixed(4)}</div>
            </>
          ) : (
            <>
              <div className="font-sans text-slate-500 mb-1">y=0 → Loss = -log(1 - ŷ) = -log({(1 - yHat).toFixed(4)})</div>
              <div className="font-bold text-amber-600">Loss = {loss.toFixed(4)}</div>
            </>
          )}
        </Expand>
      </div>
    </div>
  );
}

function GradientSection({ epoch }) {
  const snap = trainingHistory[Math.min(epoch, trainingHistory.length - 1)];
  const next = trainingHistory[Math.min(epoch + 1, trainingHistory.length - 1)];
  const d = snap.details;

  return (
    <div className="rounded-xl border-2 border-violet-300 bg-gradient-to-r from-violet-50 to-purple-50 p-4 mb-4">
      <div className="flex items-center gap-2 mb-3">
        <span className="text-lg">🔧</span>
        <h3 className="text-sm font-bold text-violet-800">Computing Average Gradient & Updating Weights</h3>
        <span className="text-xs bg-violet-100 text-violet-600 px-2 py-0.5 rounded-full">α = {LR}</span>
      </div>

      {/* STEP 1: Per-chicken error × feature */}
      <div className="bg-white rounded-lg p-3 border border-violet-200 mb-3">
        <div className="text-xs font-bold text-violet-600 mb-2">Step 1: For each chicken, compute error × feature</div>
        <div className="overflow-x-auto">
          <table className="text-xs w-full">
            <thead>
              <tr className="text-slate-400 border-b border-slate-100">
                <th className="text-left py-1 pr-2">Chicken</th>
                <th className="text-left py-1 px-2">error (ŷ - y)</th>
                <th className="text-left py-1 px-2">× weight (x₁)</th>
                <th className="text-left py-1 px-2">× thickness (x₂)</th>
                <th className="text-left py-1 px-2">gw₁</th>
                <th className="text-left py-1 px-2">gw₂</th>
              </tr>
            </thead>
            <tbody>
              {chickens.map((c, i) => (
                <tr key={c.id} className="border-b border-slate-50">
                  <td className="py-1 pr-2 font-medium text-slate-700">{c.cut}</td>
                  <td className="py-1 px-2 font-mono">{d[i].yHat.toFixed(4)} - {c.label} = <span className={d[i].error >= 0 ? "text-red-600" : "text-emerald-600"}>{d[i].error >= 0 ? "+" : ""}{d[i].error.toFixed(4)}</span></td>
                  <td className="py-1 px-2 font-mono text-slate-400">× {c.weight}</td>
                  <td className="py-1 px-2 font-mono text-slate-400">× {c.thickness}</td>
                  <td className="py-1 px-2 font-mono font-bold">{d[i].gw1 >= 0 ? "+" : ""}{d[i].gw1.toFixed(4)}</td>
                  <td className="py-1 px-2 font-mono font-bold">{d[i].gw2 >= 0 ? "+" : ""}{d[i].gw2.toFixed(4)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* STEP 2: Sum */}
      <div className="bg-white rounded-lg p-3 border border-violet-200 mb-3">
        <div className="text-xs font-bold text-violet-600 mb-2">Step 2: Sum all per-chicken gradients</div>
        <div className="text-xs font-mono text-slate-600">
          <div>Sum gw₁ = {d.map(x => `(${x.gw1 >= 0 ? "+" : ""}${x.gw1.toFixed(4)})`).join(" + ")} = <strong>{snap.sumGW1 >= 0 ? "+" : ""}{snap.sumGW1.toFixed(4)}</strong></div>
          <div className="mt-1">Sum gw₂ = {d.map(x => `(${x.gw2 >= 0 ? "+" : ""}${x.gw2.toFixed(4)})`).join(" + ")} = <strong>{snap.sumGW2 >= 0 ? "+" : ""}{snap.sumGW2.toFixed(4)}</strong></div>
        </div>
      </div>

      {/* STEP 3: Divide by 5 */}
      <div className="bg-white rounded-lg p-3 border border-violet-200 mb-3">
        <div className="text-xs font-bold text-violet-600 mb-2">Step 3: Divide by 5 → Average Gradient</div>
        <div className="text-xs font-mono text-slate-600">
          <div>Avg gw₁ = {snap.sumGW1 >= 0 ? "+" : ""}{snap.sumGW1.toFixed(4)} ÷ 5 = <strong className="text-violet-700">{snap.avgGW1 >= 0 ? "+" : ""}{snap.avgGW1.toFixed(6)}</strong></div>
          <div className="mt-1">Avg gw₂ = {snap.sumGW2 >= 0 ? "+" : ""}{snap.sumGW2.toFixed(4)} ÷ 5 = <strong className="text-violet-700">{snap.avgGW2 >= 0 ? "+" : ""}{snap.avgGW2.toFixed(6)}</strong></div>
          <div className="mt-1">Avg gb = {snap.sumGB >= 0 ? "+" : ""}{snap.sumGB.toFixed(4)} ÷ 5 = <strong className="text-violet-700">{snap.avgGB >= 0 ? "+" : ""}{snap.avgGB.toFixed(6)}</strong></div>
        </div>
      </div>

      {/* STEP 4: Update weights */}
      <div className="bg-white rounded-lg p-3 border-2 border-violet-400 mb-3">
        <div className="text-xs font-bold text-violet-600 mb-2">Step 4: new weight = old weight − (α × avg gradient)</div>
        <div className="space-y-2">
          <div className="p-2 rounded bg-amber-50 border border-amber-200">
            <div className="text-xs font-bold text-amber-600">🧂 Salt (w₁):</div>
            <div className="text-xs font-mono text-slate-700 mt-0.5">
              {snap.w1.toFixed(4)} − ({LR} × {snap.avgGW1 >= 0 ? "+" : ""}{snap.avgGW1.toFixed(6)}) = {snap.w1.toFixed(4)} − ({(LR * snap.avgGW1) >= 0 ? "+" : ""}{(LR * snap.avgGW1).toFixed(6)}) = <strong className="text-amber-700">{next.w1.toFixed(6)}</strong>
            </div>
          </div>
          <div className="p-2 rounded bg-stone-50 border border-stone-200">
            <div className="text-xs font-bold text-stone-600">🌶️ Pepper (w₂):</div>
            <div className="text-xs font-mono text-slate-700 mt-0.5">
              {snap.w2.toFixed(4)} − ({LR} × {snap.avgGW2 >= 0 ? "+" : ""}{snap.avgGW2.toFixed(6)}) = {snap.w2.toFixed(4)} − ({(LR * snap.avgGW2) >= 0 ? "+" : ""}{(LR * snap.avgGW2).toFixed(6)}) = <strong className="text-stone-700">{next.w2.toFixed(6)}</strong>
            </div>
          </div>
          <div className="p-2 rounded bg-indigo-50 border border-indigo-200">
            <div className="text-xs font-bold text-indigo-600">✨ Base (b):</div>
            <div className="text-xs font-mono text-slate-700 mt-0.5">
              {snap.b.toFixed(4)} − ({LR} × {snap.avgGB >= 0 ? "+" : ""}{snap.avgGB.toFixed(6)}) = {snap.b.toFixed(4)} − ({(LR * snap.avgGB) >= 0 ? "+" : ""}{(LR * snap.avgGB).toFixed(6)}) = <strong className="text-indigo-700">{next.b.toFixed(6)}</strong>
            </div>
          </div>
        </div>
      </div>

      {/* Tonight → Tomorrow */}
      <div className="flex items-center justify-center gap-3">
        <div className="text-center p-2 rounded-lg bg-slate-100 border">
          <div className="text-xs text-slate-400 font-bold">Night {epoch}</div>
          <div className="font-mono text-xs">🧂{snap.w1.toFixed(4)} 🌶️{snap.w2.toFixed(4)} ✨{snap.b >= 0 ? "+" : ""}{snap.b.toFixed(4)}</div>
          <div className="text-xs text-slate-400">avg loss: {snap.avgLoss.toFixed(4)}</div>
        </div>
        <div className="text-2xl text-violet-500">→</div>
        <div className="text-center p-2 rounded-lg bg-violet-100 border border-violet-300">
          <div className="text-xs text-violet-500 font-bold">Night {epoch + 1}</div>
          <div className="font-mono text-xs font-bold text-violet-700">🧂{next.w1.toFixed(4)} 🌶️{next.w2.toFixed(4)} ✨{next.b >= 0 ? "+" : ""}{next.b.toFixed(4)}</div>
          <div className="text-xs text-violet-400">cook with these tomorrow</div>
        </div>
      </div>

      <Expand title="Why subtract?">
        <div className="font-sans">
          <p>Positive gradient → that dial made predictions too high → <strong>subtract to reduce it</strong>.</p>
          <p className="mt-1">Negative gradient → that dial wasn't contributing enough → subtracting a negative <strong>adds to it</strong>.</p>
          <p className="mt-1">α = {LR} controls how big each nudge is.</p>
        </div>
      </Expand>
    </div>
  );
}

function RecipeCard({ epoch }) {
  const snap = trainingHistory[Math.min(epoch, trainingHistory.length - 1)];
  const converged = snap.correct === 5 && snap.avgLoss < 0.3;
  return (
    <div className={`rounded-2xl p-4 border-2 ${converged ? "border-emerald-400 bg-gradient-to-br from-emerald-50 to-amber-50" : "border-slate-200 bg-white"}`}>
      <div className="flex items-center gap-2 mb-3">
        <span className="text-xl">{converged ? "🏆" : "📝"}</span>
        <h3 className="text-base font-bold text-slate-800">{converged ? "Recipe Converging! All Customers Happy" : `Current Recipe — Night ${epoch}`}</h3>
      </div>
      <div className="bg-white rounded-xl p-4 border border-slate-200">
        <div className="flex gap-5 flex-wrap">
          <div className="flex items-center gap-2">
            <span className="text-lg">🧂</span>
            <div><div className="text-lg font-bold text-slate-800">{snap.w1.toFixed(3)} tsp/lb</div><div className="text-xs text-slate-400">salt</div></div>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-lg">🌶️</span>
            <div><div className="text-lg font-bold text-slate-800">{snap.w2.toFixed(3)} tsp/in</div><div className="text-xs text-slate-400">pepper</div></div>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-lg">✨</span>
            <div><div className="text-lg font-bold text-slate-800">{snap.b.toFixed(3)} tsp</div><div className="text-xs text-slate-400">base</div></div>
          </div>
        </div>
        {converged && (
          <div className="mt-3 pt-3 border-t border-emerald-200">
            <div className="grid grid-cols-2 gap-2">
              {chickens.filter(c => c.label === 1).map(c => {
                const total = snap.w1 * c.weight + snap.w2 * c.thickness + snap.b;
                return (
                  <div key={c.id} className="bg-emerald-50 rounded-lg p-2 text-xs">
                    <div className="font-bold text-emerald-700">🍗 {c.cut} ({c.weight}lbs, {c.thickness}″)</div>
                    <div className="text-slate-600">🧂{(snap.w1 * c.weight).toFixed(2)} + 🌶️{(snap.w2 * c.thickness).toFixed(2)} + ✨{snap.b.toFixed(2)} = <strong>{total.toFixed(2)} tsp</strong></div>
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default function App() {
  const [epoch, setEpoch] = useState(0);
  const snap = trainingHistory[Math.min(epoch, trainingHistory.length - 1)];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-orange-50 p-4">
      <div className="max-w-5xl mx-auto">
        <div className="text-center mb-4">
          <h1 className="text-2xl font-bold text-slate-800">👨‍🍳 The Chef's Kitchen — Logistic Regression</h1>
          <p className="text-slate-500 mt-1 text-sm">Observe → Season → Sigmoid → Confidence → Loss → <strong>Compute Avg Gradient → Update Weights</strong></p>
          <p className="text-xs text-indigo-400 mt-1">Click ▶ to expand math at any step</p>
        </div>

        {epoch === 0 && (
          <div className="bg-amber-50 border border-amber-200 rounded-xl p-3 mb-4 text-sm text-amber-800">
            <strong>Night 0:</strong> Cookbook says ¾ tsp salt/lb but ignores <strong>thickness</strong>. Pepper dial starts at 0.
          </div>
        )}
        {epoch > 0 && snap.correct < 5 && (
          <div className="bg-sky-50 border border-sky-200 rounded-xl p-3 mb-4 text-sm text-sky-800">
            <strong>Night {epoch}:</strong> Pepper dial climbing → {snap.w2.toFixed(3)} tsp/in. Learning that thickness matters.
          </div>
        )}
        {snap.correct === 5 && (
          <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-3 mb-4 text-sm text-emerald-800">
            <strong>Night {epoch}: 5/5 correct!</strong> Avg loss = {snap.avgLoss.toFixed(4)}. Every customer smiles.
          </div>
        )}

        {/* Dials */}
        <div className="flex justify-center gap-3 mb-4 flex-wrap">
          <div className="bg-amber-50 rounded-xl px-3 py-2 border border-amber-200 text-center">
            <div className="text-xs font-bold text-amber-400">🧂 w₁</div>
            <div className="text-lg font-bold text-amber-700">{snap.w1.toFixed(4)}</div>
            <div className="text-xs text-slate-400">tsp/lb</div>
          </div>
          <div className="bg-stone-100 rounded-xl px-3 py-2 border border-stone-300 text-center">
            <div className="text-xs font-bold text-stone-400">🌶️ w₂</div>
            <div className="text-lg font-bold text-stone-700">{snap.w2.toFixed(4)}</div>
            <div className="text-xs text-slate-400">tsp/in</div>
          </div>
          <div className="bg-indigo-50 rounded-xl px-3 py-2 border border-indigo-200 text-center">
            <div className="text-xs font-bold text-indigo-400">✨ b</div>
            <div className="text-lg font-bold text-indigo-700">{snap.b.toFixed(4)}</div>
            <div className="text-xs text-slate-400">tsp</div>
          </div>
          <div className="bg-violet-50 rounded-xl px-3 py-2 border border-violet-200 text-center">
            <div className="text-xs font-bold text-violet-400">α</div>
            <div className="text-lg font-bold text-violet-700">{LR}</div>
            <div className="text-xs text-slate-400">learn rate</div>
          </div>
          <div className="bg-rose-50 rounded-xl px-3 py-2 border border-rose-200 text-center">
            <div className="text-xs font-bold text-rose-400">📉 avg loss</div>
            <div className="text-lg font-bold text-rose-700">{snap.avgLoss.toFixed(4)}</div>
          </div>
          <div className="bg-emerald-50 rounded-xl px-3 py-2 border border-emerald-200 text-center">
            <div className="text-xs font-bold text-emerald-400">🌙 Night {epoch}</div>
            <div className="text-lg font-bold text-emerald-700">{snap.correct}/5</div>
          </div>
        </div>

        {/* Chicken rows */}
        <div className="mb-3">
          {chickens.map((c, i) => <ChickenRow key={c.id} chicken={c} detail={snap.details[i]} weights={snap} />)}
        </div>

        {/* Average loss */}
        <div className="rounded-xl border-2 border-orange-300 bg-orange-50 p-3 mb-3 flex items-center gap-4">
          <div className="flex-1 text-xs font-mono text-slate-600">
            Avg Loss = ({snap.details.map(d => d.loss.toFixed(3)).join(" + ")}) ÷ 5
          </div>
          <div className={`text-2xl font-bold ${snap.avgLoss > 0.4 ? "text-red-600" : snap.avgLoss > 0.2 ? "text-amber-600" : "text-emerald-600"}`}>
            = {snap.avgLoss.toFixed(4)}
          </div>
        </div>

        {/* Gradient computation + weight update */}
        <GradientSection epoch={epoch} />

        {/* Controls */}
        <div className="flex justify-center items-center gap-2 mb-5">
          <button onClick={() => setEpoch(0)} className="px-3 py-1.5 rounded-lg bg-slate-200 text-slate-600 text-sm font-semibold hover:bg-slate-300">Reset</button>
          <button onClick={() => setEpoch(Math.max(0, epoch - 1))} className="px-3 py-1.5 rounded-lg bg-slate-200 text-slate-700 text-sm font-semibold hover:bg-slate-300">← Prev</button>
          <div className="text-sm text-slate-500 font-medium px-2">Night {epoch}/20</div>
          <button onClick={() => setEpoch(Math.min(20, epoch + 1))} className="px-3 py-1.5 rounded-lg bg-indigo-500 text-white text-sm font-semibold hover:bg-indigo-600">Next →</button>
          <button onClick={() => setEpoch(20)} className="px-3 py-1.5 rounded-lg bg-emerald-500 text-white text-sm font-semibold hover:bg-emerald-600">Skip to end</button>
        </div>

        <RecipeCard epoch={epoch} />
      </div>
    </div>
  );
}
