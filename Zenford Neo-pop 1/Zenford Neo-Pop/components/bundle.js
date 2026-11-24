/* @ds-bundle: {"format": 4, "namespace": "ZenfordNP", "components": [{"name": "Button"}, {"name": "Card"}, {"name": "Overline"}, {"name": "Tag"}, {"name": "Pill"}, {"name": "Switch"}, {"name": "ProgressBar"}, {"name": "AnswerOption"}, {"name": "LangTile"}, {"name": "ZenSay"}]} */
(function(){
/* ===== Zen: SVG mascot with LED states, cursor-follow eyes and blinking ===== */
const K='#141414',Y='#FDE047';
const ZEYES={
 normal:`<rect x="68" y="88" width="18" height="12" rx="6" fill="${Y}"/><rect x="114" y="88" width="18" height="12" rx="6" fill="${Y}"/>`,
 happy:`<path d="M68 98q9-13 18 0M114 98q9-13 18 0" stroke="${Y}" stroke-width="5" fill="none" stroke-linecap="round"/>`,
 wow:`<circle cx="77" cy="93" r="8" fill="${Y}"/><circle cx="123" cy="93" r="8" fill="${Y}"/>`,
 wink:`<path d="M68 97q9-12 18 0" stroke="${Y}" stroke-width="5" fill="none" stroke-linecap="round"/><rect x="114" y="88" width="18" height="12" rx="6" fill="${Y}"/>`,
 think:`<rect x="76" y="82" width="14" height="10" rx="5" fill="${Y}"/><rect x="120" y="82" width="14" height="10" rx="5" fill="${Y}"/>`,
 love:`<path d="M77 101l-8-8a4.6 4.6 0 0 1 8-5 4.6 4.6 0 0 1 8 5z M123 101l-8-8a4.6 4.6 0 0 1 8-5 4.6 4.6 0 0 1 8 5z" fill="${Y}"/>`,
 sad:`<path d="M68 90q9 10 18 0M114 90q9 10 18 0" stroke="${Y}" stroke-width="5" fill="none" stroke-linecap="round"/>`,
 blink:`<path d="M68 96h18M114 96h18" stroke="${Y}" stroke-width="5" stroke-linecap="round"/>`,
 fierce:`<path d="M66 86l22 6v8H66z M134 86l-22 6v8h22z" fill="${Y}"/>`
};
const ZMOUTH={normal:'smile',happy:'grin',wow:'o',wink:'tongue',think:'flat',love:'grin',sad:'down',blink:'smile',fierce:'grin'};
const MOUTHS={smile:`<path d="M90 112q10 8 20 0" stroke="${Y}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
 grin:`<path d="M86 110q14 13 28 0z" fill="${Y}"/>`,o:`<circle cx="100" cy="114" r="5" stroke="${Y}" stroke-width="3.5" fill="none"/>`,
 flat:`<path d="M92 114h16" stroke="${Y}" stroke-width="4" stroke-linecap="round"/>`,down:`<path d="M90 117q10-7 20 0" stroke="${Y}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
 tongue:`<path d="M90 110q10 8 20 0" stroke="${Y}" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M100 114q0 8 5 8t4-8" fill="#FF9F8A" stroke="${K}" stroke-width="2"/>`};
const ZACC={
 cape:{back:`<path d="M60 150h80l30 64q-70 14-140 0z" fill="#2F4BD8" stroke="${K}" stroke-width="5" stroke-linejoin="round"/><path d="M92 196h16l-16 12h16" stroke="${Y}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`},
 phones:{mid:`<path d="M36 96Q36 22 100 22T164 96" stroke="${K}" stroke-width="9" fill="none"/><path d="M36 96Q36 22 100 22T164 96" stroke="#D8CCFF" stroke-width="4" fill="none"/>`,front:`<rect x="20" y="78" width="22" height="40" rx="9" fill="#D8CCFF" stroke="${K}" stroke-width="5"/><rect x="158" y="78" width="22" height="40" rx="9" fill="#D8CCFF" stroke="${K}" stroke-width="5"/>`},
 tv:{mid:`<path d="M100 48L78 16M100 48L122 16" stroke="${K}" stroke-width="5" stroke-linecap="round"/><circle cx="78" cy="14" r="7" fill="${Y}" stroke="${K}" stroke-width="4"/><circle cx="122" cy="14" r="10" fill="${Y}" stroke="${K}" stroke-width="4"/><path d="M118 10h8l-8 8h8" stroke="${K}" stroke-width="2.5" fill="none"/>`,noAnt:true},
 pencil:{holdR:true,front:`<g transform="rotate(-35 168 168)"><rect x="160" y="120" width="14" height="62" rx="3" fill="${Y}" stroke="${K}" stroke-width="4"/><path d="M160 182l7 16 7-16z" fill="#FFD2B8" stroke="${K}" stroke-width="4" stroke-linejoin="round"/></g>`},
 mic:{holdR:true,front:`<path d="M166 196L172 150" stroke="${K}" stroke-width="6" stroke-linecap="round"/><circle cx="173" cy="140" r="13" fill="#BDEFD8" stroke="${K}" stroke-width="5"/>`},
 book:{front:`<path d="M58 170q21-8 42 0q21-8 42 0v34q-21-8-42 0q-21-8-42 0z" fill="#FFF1A8" stroke="${K}" stroke-width="5" stroke-linejoin="round"/><path d="M100 170v34" stroke="${K}" stroke-width="4"/>`},
 helmet:{mid:`<path d="M30 92Q30 30 100 28T170 92z" fill="#FFFFFF" stroke="${K}" stroke-width="5.5" stroke-linejoin="round"/><path d="M92 30h16v58H92z" fill="${Y}" stroke="${K}" stroke-width="3"/>`,noEars:true,noAnt:true}
};
function zenSVG(state,hood,acc,label){
  const a=ZACC[acc]||{},hd=hood||'#BFE4FF';
  const ears=a.noEars?'':`<path d="M42 66 48 20 86 50Z M158 66 152 20 114 50Z" fill="#FFFFFF" stroke="${K}" stroke-width="5" stroke-linejoin="round"/><path d="M50 56 52 34 70 48Z M150 56 148 34 130 48Z" fill="${Y}"/>`;
  const ant=a.noAnt?'':`<path d="M100 28v18" stroke="${K}" stroke-width="5" stroke-linecap="round"/><circle cx="100" cy="24" r="7" fill="${Y}" stroke="${K}" stroke-width="4"/>`;
  const tail=`<path d="M146 192q30 4 30-22q0-14-12-12" stroke="${K}" stroke-width="11" fill="none" stroke-linecap="round"/><path d="M146 192q30 4 30-22q0-14-12-12" stroke="${hd}" stroke-width="5" fill="none" stroke-linecap="round"/>`;
  const legs=`<rect x="70" y="196" width="22" height="20" rx="8" fill="#FFFFFF" stroke="${K}" stroke-width="5"/><rect x="108" y="196" width="22" height="20" rx="8" fill="#FFFFFF" stroke="${K}" stroke-width="5"/>`;
  const armL=a.waveL?'':`<path d="M58 162q-16 8-14 26" stroke="${K}" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M58 162q-16 8-14 26" stroke="${hd}" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="44" cy="190" r="8" fill="#fff" stroke="${K}" stroke-width="4.5"/>`;
  const armR=a.holdR?'':`<path d="M142 162q16 8 14 26" stroke="${K}" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M142 162q16 8 14 26" stroke="${hd}" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="156" cy="190" r="8" fill="#fff" stroke="${K}" stroke-width="4.5"/>`;
  return `<svg class="zen" viewBox="0 0 200 222" role="img" aria-label="${label||'Zen, mèo robot của Zenford'}">${a.back||''}${tail}${legs}${ant}${ears}
   <path d="M60 148h80a14 14 0 0 1 14 14v26a12 12 0 0 1-12 12H58a12 12 0 0 1-12-12v-26a14 14 0 0 1 14-14z" fill="${hd}" stroke="${K}" stroke-width="5.5"/>
   <path d="M88 160h24l-24 18h24" stroke="${K}" stroke-width="4.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
   ${armL}${armR}
   <rect x="34" y="48" width="132" height="98" rx="30" fill="#FFFFFF" stroke="${K}" stroke-width="5.5"/>${a.mid||''}
   <rect x="50" y="64" width="100" height="64" rx="18" fill="#111111"/>
   <circle cx="58" cy="118" r="5" fill="#FF9F8A" opacity=".85"/><circle cx="142" cy="118" r="5" fill="#FF9F8A" opacity=".85"/>
   <g class="zface" data-state="${state||'normal'}"><g class="zeyes">${ZEYES[state]||ZEYES.normal}</g><g class="zmouth">${MOUTHS[ZMOUTH[state]||'smile']}</g></g>${a.front||''}</svg>`;
}
function setZen(host,state){const f=host.querySelector('.zface');if(!f)return;f.dataset.state=state;f.querySelector('.zeyes').innerHTML=ZEYES[state]||ZEYES.normal;f.querySelector('.zmouth').innerHTML=MOUTHS[ZMOUTH[state]||'smile'];}
function mountZens(root){root.querySelectorAll('[data-zen]').forEach(el=>{const [s,h,a]=el.dataset.zen.split('|');el.innerHTML=zenSVG(s,h,a==='follow'?'':a);if(a==='follow')el.classList.add('zfollow');});}
function logoSVG(fill,size){return `<svg width="${size}" height="${size}" viewBox="0 0 48 48" aria-hidden="true" style="transform:rotate(-8deg);flex:none"><path d="M10 15 12 4 20 11Z M38 15 36 4 28 11Z" fill="${fill}" stroke="${K}" stroke-width="2.4" stroke-linejoin="round"/><path d="M12 9h24a8 8 0 0 1 8 8v13a8 8 0 0 1-8 8H22l-8 7v-7h-2a8 8 0 0 1-8-8V17a8 8 0 0 1 8-8z" fill="${fill}" stroke="${K}" stroke-width="2.6" stroke-linejoin="round"/><path d="M17 17h14L17 31h14" stroke="${fill==='#2F4BD8'?Y:K}" stroke-width="3.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>`;}
function mountLogos(root){root.querySelectorAll('[data-logo]').forEach(el=>{if(el.querySelector('svg'))return;el.insertAdjacentHTML('afterbegin',logoSVG(el.dataset.logo,el.classList.contains('brand')?34:22));});}


var REDUCE=typeof matchMedia==='function'&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function mount(root){root=root||document;mountLogos(root);mountZens(root);}
var following=false;
function followEyes(){if(following)return;following=true;addEventListener('pointermove',function(e){
  document.querySelectorAll('.zfollow .zeyes').forEach(function(g){var svg=g.ownerSVGElement,r=svg.getBoundingClientRect();if(!r.width)return;
    var cx=r.left+r.width/2,cy=r.top+r.height*.42,dx=e.clientX-cx,dy=e.clientY-cy,d=Math.hypot(dx,dy)||1,m=Math.min(7,d/40);
    g.setAttribute('transform','translate('+(dx/d*m).toFixed(1)+' '+(dy/d*m*.7).toFixed(1)+')');});},{passive:true});}
var blinking=false;
function blink(){if(blinking||REDUCE)return;blinking=true;setInterval(function(){document.querySelectorAll('.zface').forEach(function(f){var s=f.dataset.state;if(s!=='normal'&&s!=='happy'&&s!=='fierce')return;if(Math.random()<.35){var e=f.querySelector('.zeyes');e.innerHTML=ZEYES.blink;setTimeout(function(){if(f.dataset.state===s)e.innerHTML=ZEYES[s];},140);}});},2600);}
window.ZenfordNP={zenSVG:zenSVG,setZen:setZen,logoSVG:logoSVG,mount:mount,followEyes:followEyes,blink:blink,
  states:Object.keys(ZEYES).filter(function(k){return k!=='blink'}),outfits:Object.keys(ZACC)};
})();
