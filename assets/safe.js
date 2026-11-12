/* Public guide: menu and suggestion choices only. Never submit private data. */
(function(){
  // Navigation stays visible without JavaScript, including on narrow screens.
  document.documentElement.classList.add('js');
  const toggle=document.querySelector('.menu');
  if(toggle) toggle.addEventListener('click',()=>{
    const nav=document.querySelector('.nav'), open=nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded',String(open));
  });
  const choices=document.querySelectorAll('[data-suggestion]');
  if(!choices.length) return;
  const key='tino2-public-suggestions-v2';
  let saved={};
  try{saved=JSON.parse(localStorage.getItem(key)||'{}')||{};}catch(e){saved={};}
  choices.forEach(el=>{
    if(['consider','defer','decline','privacy','decision','risk','presentation'].includes(saved[el.dataset.suggestion])) el.value=saved[el.dataset.suggestion];
    el.addEventListener('change',()=>{
      saved[el.dataset.suggestion]=el.value;
      try{localStorage.setItem(key,JSON.stringify(saved));document.getElementById('save-status').textContent='Selection saved in this browser only.';}
      catch(e){document.getElementById('save-status').textContent='Browser storage unavailable; selection is temporary.';}
    });
  });
  const reset=document.getElementById('clear-selections');
  if(reset) reset.addEventListener('click',()=>{
    saved={};choices.forEach(el=>el.value='');try{localStorage.removeItem(key);}catch(e){}
    document.getElementById('save-status').textContent='Selections cleared from this browser.';
  });
})();
