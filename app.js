let toggler = document.getElementById("toggler")
let closeTog = document.querySelector(".closeMenu span i")
let closeLink = document.querySelectorAll(".menuItms")
let header = document.querySelector(".salam")
let headerR = document.querySelector(".xulase")
let headerP = document.querySelector(".layiheler")
let headerB = document.querySelector(".blog")
let headerC = document.querySelector(".elaqe")
let headerY = document.querySelector(".yusif")


const typedTextSpan = document.querySelector(".typed-text");
const cursorSpan = document.querySelector(".cursorJ");

const textArray = ["hard", "fun", "a journey", "LIFE"];
const typingDelay = 200;
const erasingDelay = 100;
const newTextDelay = 2000; // Delay between current and next text
let textArrayIndex = 0;
let charIndex = 0;

function type() {
  if (charIndex < textArray[textArrayIndex].length) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, typingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
    setTimeout(erase, newTextDelay);
  }
}

function erase() {
  if (charIndex > 0) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex-1);
    charIndex--;
    setTimeout(erase, erasingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
    textArrayIndex++;
    if(textArrayIndex>=textArray.length) textArrayIndex=0;
    setTimeout(type, typingDelay + 1100);
  }
}

document.addEventListener("DOMContentLoaded", function() { // On DOM Load initiate the effect
  if(textArray.length) setTimeout(type, newTextDelay + 250);
});

let textArrayH = ["Salam_"]
let textArrayR = ["Xülasə_"]
let textArrayP = ["Layihələrim_"]
let textArrayB = ["Blog_"]
let textArrayC = ["Əlaqə_"]
let textArrayY = ["Yusif Osmanov_"]


let textArrayIndexH = 0;
let charIndexH = 0;
let textArrayIndexR = 0;
let charIndexR = 0;
let textArrayIndexP = 0;
let charIndexP = 0;
let textArrayIndexB = 0;
let charIndexB = 0;
let textArrayIndexC = 0;
let charIndexC = 0;
let textArrayIndexY = 0;
let charIndexY = 0;

toggler.addEventListener('click',function(){
    let overlay = document.querySelector(".overlay")
    overlay.style.opacity = "1";
    overlay.style.visibility = "visible";
    overlay.style.transition = "all .3s ease"
})

closeTog.addEventListener('click',()=>{
    let overlay = document.querySelector(".overlay")
    overlay.style.opacity = "0";
    overlay.style.visibility = "hidden";
    overlay.style.transition = "all .3s ease"
})

closeLink.forEach(function(element,index){
  element.querySelector(".linK").addEventListener('click',function(){
    this.parentElement.parentElement.parentElement.style.opacity="0";
    this.parentElement.parentElement.parentElement.style.visibility="hidden";
    this.parentElement.parentElement.parentElement.style.transition = "all .3s ease"
  })
})


function typeH(){ 
    if(charIndexH<textArrayH[textArrayIndexH].length){
        
        header.textContent += textArrayH[textArrayIndexH].charAt(charIndexH);
        
        charIndexH++;
        setTimeout(typeH, typingDelay);
        
    }
 }

 typeH();

 function typeR(){ 
    if(charIndexR<textArrayR[textArrayIndexR].length){
        
        headerR.textContent += textArrayR[textArrayIndexR].charAt(charIndexR);
        
        charIndexR++;
        setTimeout(typeR, typingDelay);
        
    }
 }

 function typeP(){ 
    if(charIndexP<textArrayP[textArrayIndexP].length){
        headerP.textContent += textArrayP[textArrayIndexP].charAt(charIndexP);
        
        charIndexP++;
        setTimeout(typeP, typingDelay);
        
    }
 }

 function typeB(){ 
    if(charIndexB<textArrayB[textArrayIndexB].length){
        headerB.textContent += textArrayB[textArrayIndexB].charAt(charIndexB);
        
        charIndexB++;
        setTimeout(typeB, typingDelay);
        
    }
 }
 
 function typeC(){ 
    if(charIndexC<textArrayC[textArrayIndexC].length){
        
        headerC.textContent += textArrayC[textArrayIndexC].charAt(charIndexC);
        
        charIndexC++;
        setTimeout(typeC, typingDelay);
        
    }
 }

 function typeY(){ 
    if(charIndexY<textArrayY[textArrayIndexY].length){
        
        headerY.textContent += textArrayY[textArrayIndexY].charAt(charIndexY);
        
        charIndexY++;
        setTimeout(typeY, typingDelay);
        
    }
 }


typeY()

 window.addEventListener("scroll",()=>{
     var headerNav =document.querySelector("#navbarNav");
     headerNav.classList.toggle("sticky",window.scrollY>0);
    let scrolled = window.scrollY;
    
    if(scrolled > 200){
        typeR()
        
    }
    if(scrolled > 1450){
        typeP()
    }
    if(scrolled > 3550){
        typeB()
    }
    if(scrolled > 4300){
        typeC()
    }

 })
