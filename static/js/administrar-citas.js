const sweetAlert = (text, confirmButtonText, confirmButtonColor, evento) => {
  Swal.fire({
    icon: "question",
    titleText: '¿Está seguro?',
    text: text,
    showCancelButton: true,
    cancelButtonText: "Cancelar",
    cancelButtonColor: "#6c757d",
    confirmButtonText: confirmButtonText,
    confirmButtonColor: confirmButtonColor,
    backdrop: true,
    showLoaderOnConfirm: true,
    preConfirm: () => {
      location.href = evento.target.href;
    },
    allowOutsideClick: () => false,
    allowEscapeKey: () => false,
  });
};

const enlacesAceptar = document.querySelectorAll(".aceptar-cita");
const enlacesRechazar = document.querySelectorAll(".rechazar-cita");
const enlacesQuitarCitaAceptada = document.querySelectorAll(".quitar-cita-aceptada");
const enlacesQuitarCitaRechazada = document.querySelectorAll(".quitar-cita-rechazada");

enlacesAceptar.forEach((enlace) => {
  enlace.addEventListener("click", (evento) => {
    evento.preventDefault();
    sweetAlert("¿Quiere aceptar esta cita?", "Aceptar", "#28a745", evento);
  });
});

enlacesRechazar.forEach((enlace) => {
  enlace.addEventListener("click", (evento) => {
    evento.preventDefault();
    sweetAlert("¿Quiere rechazar esta cita?", "Rechazar", "#dc3545", evento);
  });
});

enlacesQuitarCitaAceptada.forEach((enlace) => {
  enlace.addEventListener("click", (evento) => {
    evento.preventDefault();
    sweetAlert("¿Quiere quitar esta cita de las citas aceptadas?", "Quitar", "#007bff", evento);
  });
});

enlacesQuitarCitaRechazada.forEach((enlace) => {
  enlace.addEventListener("click", (evento) => {
    evento.preventDefault();
    sweetAlert("¿Quiere quitar esta cita de las citas rechazadas?", "Quitar", "#007bff", evento);
  });
});
