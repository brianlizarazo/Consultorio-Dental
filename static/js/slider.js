const slider = document.getElementById("slider");
let sliderElemento = document.querySelectorAll(".slider-elemento");
let ultimoSliderElemento = sliderElemento[sliderElemento.length - 1];

const botonIzquierdo = document.getElementById("boton-izquierda");
const botonDerecho = document.getElementById("boton-derecha");

slider.insertAdjacentElement("afterbegin", ultimoSliderElemento);

function moverDerecha() {
  let primerSliderElemento = document.querySelectorAll(".slider-elemento")[0];
  botonDerecho.style.display = "none";
  slider.style.marginLeft = "-200%";
  slider.style.transition = "all 0.5s ease";
  setTimeout(function () {
    slider.style.transition = "none";
    slider.insertAdjacentElement("beforeend", primerSliderElemento);
    slider.style.marginLeft = "-100%";
    botonDerecho.style.display = "flex";
  }, 500);
}

function moverIzquierda() {
  let sliderElemento = document.querySelectorAll(".slider-elemento");
  let ultimoSliderElemento = sliderElemento[sliderElemento.length - 1];
  botonIzquierdo.style.display = "none";
  slider.style.marginLeft = "0";
  slider.style.transition = "all 0.5s ease";
  setTimeout(function () {
    slider.style.transition = "none";
    slider.insertAdjacentElement("afterbegin", ultimoSliderElemento);
    slider.style.marginLeft = "-100%";
    botonIzquierdo.style.display = "flex";
  }, 500);
}

function ocultarBotones() {
  botonDerecho.style.display = "none";
  botonIzquierdo.style.display = "none";
}

function mostrarBotones() {
  botonDerecho.style.display = "flex";
  botonIzquierdo.style.display = "flex";
}

function moverSlider() {
  ocultarBotones();
  moverDerecha();
  setTimeout(function () {
    mostrarBotones();
  }, 500);
}

var temporizadorSlider = setInterval(moverSlider, 5000);

botonDerecho.addEventListener("click", () => {
  clearInterval(temporizadorSlider);
  temporizadorSlider = setInterval(moverSlider, 5000);
  moverDerecha();
});

botonIzquierdo.addEventListener("click", () => {
  clearInterval(temporizadorSlider);
  temporizadorSlider = setInterval(moverSlider, 5000);
  moverIzquierda();
});
