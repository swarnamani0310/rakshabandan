// petals
(function(){
  const colors = ['#e08a94','#f3cd6e','#e57f3d'];
  const n = window.innerWidth < 640 ? 8 : 14;
  for(let i=0;i<n;i++){
    const p = document.createElement('div');
    p.className = 'petal';
    p.style.left = Math.random()*100+'%';
    p.style.background = colors[i%3];
    p.style.animationDuration = (12+Math.random()*10)+'s';
    p.style.animationDelay = (Math.random()*15)+'s';
    document.body.appendChild(p);
  }
})();
