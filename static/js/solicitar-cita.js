// =============================================
//                MANIPULAR FECHA
// =============================================

// Obtener la fecha de hoy
const hoy = new Date();
// Calcular la fecha de hoy pero con un año adelante
const fechaCitaMax = new Date();
fechaCitaMax.setFullYear(fechaCitaMax.getFullYear() + 1);

// Obtener los elementos 'input' con la fecha de nacimiento y la fecha de la cita
const fechaDeNacimiento = document.getElementById("fecha-de-nacimiento");
const fechaDeCita = document.getElementById("fecha-cita");

// La fecha de nacimiento no puede ser superior al día de hoy
fechaDeNacimiento.setAttribute("max", hoy.toISOString().substring(0, 10));
// La fecha de la cita no puede ser anterior al día de hoy
fechaDeCita.setAttribute("min", hoy.toISOString().substring(0, 10));
// La fecha de la cita no puede ser superior a un año a partir de hoy
fechaDeCita.setAttribute("max", fechaCitaMax.toISOString().substring(0, 10));

// =================================================================================
//                            REGISTRAR DATOS DEL CLIENTE
// =================================================================================

// Obtener el elemento que contiene los datos personales del paciente
const datosPersonales = document.getElementById("datos-personales-cliente");

// Obtener los botones que marcan como verdadero o falso que es la primera vez solicitando una cita
const primeraVezTrue = document.getElementById("primera-vez-true");
const primeraVezFalse = document.getElementById("primera-vez-false");

// Si es la primera vez que el usuario solicita una cita, se mostrará el formulario para rellenar sus datos personales
// Si no es la primera vez, el formulario permanecerá oculto
primeraVezTrue.addEventListener("click", () => {
  datosPersonales.style.height = datosPersonales.scrollHeight + "px";
});
primeraVezFalse.addEventListener("click", () => {
  datosPersonales.style.height = 0;
});

// ======================================================
//                   REGISTRAR PARIENTE
// ======================================================

// Obtener el elemento que contiene el formulario para agregar un pariente
const agregarPariente = document.getElementById("agregar-pariente");

// Obtener los botones que marcan como verdadero o falso que el usuario tiene una pariente
const tieneParentescoTrue = document.getElementById("tiene-parentesco-true");
const tieneParentescoFalse = document.getElementById("tiene-parentesco-false");

// Si el usuario tiene parentesco con otro paciente de la clínica, se mostrará el formulario para agregar el parentesco con el paciente
// Si el usuario no tiene parentesco, el formulario permanecerá oculto
tieneParentescoTrue.addEventListener("click", () => {
  if (agregarPariente.clientHeight == 0) {
    datosPersonales.style.height = datosPersonales.scrollHeight + agregarPariente.scrollHeight + "px";
    agregarPariente.style.height = agregarPariente.scrollHeight.toString() + "px";
  }
});
tieneParentescoFalse.addEventListener("click", () => {
  if (agregarPariente.clientHeight != 0) {
    agregarPariente.style.height = 0;
    datosPersonales.style.height = datosPersonales.scrollHeight - agregarPariente.scrollHeight + "px";
  }
});

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
  datosPersonales.style.height = datosPersonales.scrollHeight + 51 + "px";
  listaTelefónos.appendChild(nuevoTeléfono);
  i++;
});

// Si el usuario presiona el botón para remover un teléfono, se elimina un 'input' de tipo teléfono
removerTeléfono.addEventListener("click", () => {
  if (i == 2) {
    removerTeléfono.style.display = "none";
  }
  listaTelefónos.removeChild(listaTelefónos.lastElementChild);
  datosPersonales.style.height = datosPersonales.scrollHeight - 51 + "px";
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
  datosPersonales.style.height = datosPersonales.scrollHeight + 51 + "px";
  listaEmails.appendChild(nuevoEmail);
  j++;
});

// Si el usuario presiona el botón para remover un email, se elimina un 'input' de tipo email
removerEmail.addEventListener("click", () => {
  if (j == 2) {
    removerEmail.style.display = "none";
  }
  listaEmails.removeChild(listaEmails.lastElementChild);
  datosPersonales.style.height = datosPersonales.scrollHeight - 51 + "px";
  j--;
});
