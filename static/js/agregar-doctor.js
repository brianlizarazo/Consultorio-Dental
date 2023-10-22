// =============================================
//                MANIPULAR FECHA
// =============================================

// Obtener la fecha de hoy
const fecha = new Date();

// Darle formato ISO a la fecha de hoy
const hoy = fecha.getFullYear().toString() + "-" + (fecha.getMonth() + 1).toString() + "-" + fecha.getDate().toString();

// Obtener el elemento 'input' con la fecha de nacimiento
const fechaDeNacimiento = document.getElementById("fecha-de-nacimiento");

// La fecha de nacimiento no puede ser superior al día de hoy
fechaDeNacimiento.setAttribute("max", hoy);

// ===============================================================
//                      ADMINISTRAR TELÉFONOS
// ===============================================================

// Obtener la lista con los 'input' de tipo teléfono
const listaTelefónos = document.getElementById("telefonos");

// Obtener los botones para agregar y remover un teléfono
const agregarTeléfono = document.getElementById("agregar-telefono");
const removerTeléfono = document.getElementById("remover-telefono");

// Crear un iterador
let i = 1;

// Si el usuario presiona el botón para agregar un teléfono, se crea un 'input' de tipo teléfono
agregarTeléfono.addEventListener("click", () => {
  if (i == 1) {
    removerTeléfono.style.display = "block";
  }
  const nuevoTeléfono = document.createElement("input");
  nuevoTeléfono.setAttribute("type", "tel");
  nuevoTeléfono.setAttribute("id", "telefono" + (i + 1));
  nuevoTeléfono.setAttribute("name", "telefono");
  nuevoTeléfono.setAttribute("class", "campo telefono");
  nuevoTeléfono.setAttribute("pattern", "[0][0-9]{3}[-][0-9]{7}");
  nuevoTeléfono.setAttribute("title", "El número de teléfono debe tener el siguiente formato: 0XXX-XXXXXXX");
  nuevoTeléfono.setAttribute("placeholder", "Número de teléfono" + " #" + (i + 1));
  listaTelefónos.appendChild(nuevoTeléfono);
  i++;
});

// Si el usuario presiona el botón para remover un teléfono, se elimina un 'input' de tipo teléfono
removerTeléfono.addEventListener("click", () => {
  if (i == 2) {
    removerTeléfono.style.display = "none";
  }
  listaTelefónos.removeChild(listaTelefónos.lastElementChild);
  i--;
});

// ======================================================
//                   ADMINISTRAR EMAILS
// ======================================================

// Obtener la lista con los 'input' de tipo correo electrónico
const listaEmails = document.getElementById("emails");

// Obtener los botones para agregar y remover un correo electrónico
const agregarEmail = document.getElementById("agregar-email");
const removerEmail = document.getElementById("remover-email");

// Crear un iterador
let j = 1;

// Si el usuario presiona el botón para agregar un email, se crea un 'input' de tipo email
agregarEmail.addEventListener("click", () => {
  if (j == 1) {
    removerEmail.style.display = "block";
  }
  const nuevoEmail = document.createElement("input");
  nuevoEmail.setAttribute("type", "email");
  nuevoEmail.setAttribute("id", "email" + (j + 1));
  nuevoEmail.setAttribute("name", "email");
  nuevoEmail.setAttribute("class", "campo email");
  nuevoEmail.setAttribute("pattern", "[a-zA-Z0-9.^_+!#$%&/='?*`}{|-]{1,64}[@][a-zA-Z0-9.-]{1,253}[.][a-z]{2,18}");
  nuevoEmail.setAttribute("title", "El correo electrónico no cumple con el formato requerido");
  nuevoEmail.setAttribute("placeholder", "Correo electrónico" + " #" + (j + 1));
  listaEmails.appendChild(nuevoEmail);
  j++;
});

// Si el usuario presiona el botón para remover un email, se elimina un 'input' de tipo email
removerEmail.addEventListener("click", () => {
  if (j == 2) {
    removerEmail.style.display = "none";
  }
  listaEmails.removeChild(listaEmails.lastElementChild);
  j--;
});
