// Se seleccionan los elementos del menú hamburguesa y la barra de navegación
const hamburguesa = document.querySelector(".hamburguesa");
const navbar = document.querySelector("nav");
const servicios = document.querySelector(".servicios");
const listaServicios = document.querySelector(".lista-servicios");
var alturaNavbar = navbar.scrollHeight;
var alturaListaServicios = listaServicios.scrollHeight;
var listaAbierta = false;

// Si se le da clic al ícono de hamburguesa, el ícono se transforma y se despliega el menú
// Si se le da clic otra vez, el ícono vuelve a la normalidad y se retrae el menú
hamburguesa.addEventListener("click", () => {
  hamburguesa.classList.toggle("activa");
  navbar.classList.toggle("activa");
  if (navbar.classList.contains("activa")) {
    navbar.style.height = navbar.scrollHeight.toString() + "px";
  } else {
    navbar.style.height = 0;
    listaServicios.classList.remove("seleccionada");
    listaServicios.removeAttribute("style");
  }
});

// Si se le da clic a alguno de los enlaces, el ícono del menú hamburguesa vuelve a la normalidad y el menú se retrae
document.querySelectorAll("nav a").forEach((a) => {
  a.addEventListener("click", () => {
    hamburguesa.classList.remove("activa");
    navbar.classList.remove("activa");
    navbar.removeAttribute("style");
  });
});

// Se crea una mediaQuery que detecta cuando hay un cambio en el tamaño de la pantalla
mediaQuery = matchMedia("(min-width: 900px)");

// Si el tamaño de la pantalla aumenta hasta los 900 px o más y el menú estaba desplegado, el ícono hamburguesa vuelve a la normalidad y se retrae el menú desplegable
mediaQuery.addEventListener("change", (e) => {
  if (mediaQuery.matches) {
    hamburguesa.classList.remove("activa");
    navbar.classList.remove("activa");
    navbar.removeAttribute("style");
    listaServicios.classList.remove("seleccionada");
    listaServicios.removeAttribute("style");
  }
});

function mostrarListaServicios () {
  listaServicios.classList.add("lista-servicios-abierta");
}

function ocultarListaServicios () {
  setTimeout(() => {
    if (!listaAbierta) {
      listaServicios.classList.remove("lista-servicios-abierta");
    }
  }, 50);
}

function marcarListaComoAbierta () {
  listaAbierta = true;
}

function marcarListaComoCerrada () {
  listaAbierta = false;
  listaServicios.classList.remove("lista-servicios-abierta");
}

function desplegarListaServicios () {
  listaServicios.classList.toggle("seleccionada");
  if (listaServicios.classList.contains("seleccionada")) {
    navbar.style.height = (alturaNavbar + alturaListaServicios).toString() + "px";
    listaServicios.style.height = alturaListaServicios.toString() + "px";
  }
  else {
    navbar.style.height = alturaNavbar.toString() + "px";
    listaServicios.style.height = 0;
  }
}

// Se ejecutará el código cuando se haya renderizado la página por completo
window.addEventListener("load", () => {
  if (mediaQuery.matches) {
    servicios.addEventListener("mouseover", mostrarListaServicios);
    servicios.addEventListener("mouseleave", ocultarListaServicios);
    listaServicios.addEventListener("mouseover", marcarListaComoAbierta);
    listaServicios.addEventListener("mouseleave", marcarListaComoCerrada);
  }
  else {
    servicios.addEventListener("click", desplegarListaServicios);
  }
});

mediaQuery.addEventListener("change", (e) => {
  alturaNavbar = navbar.scrollHeight;
  alturaListaServicios = listaServicios.scrollHeight;
  if (mediaQuery.matches) {
    servicios.removeEventListener("click", desplegarListaServicios);

    servicios.addEventListener("mouseover", mostrarListaServicios);
    servicios.addEventListener("mouseleave", ocultarListaServicios);
    listaServicios.addEventListener("mouseover", marcarListaComoAbierta);
    listaServicios.addEventListener("mouseleave", marcarListaComoCerrada);
  }
  else {
    servicios.removeEventListener("mouseover", mostrarListaServicios);
    servicios.removeEventListener("mouseleave", ocultarListaServicios);
    listaServicios.removeEventListener("mouseover", marcarListaComoAbierta);
    listaServicios.removeEventListener("mouseleave", marcarListaComoCerrada);

    servicios.addEventListener("click", desplegarListaServicios);
  }
});