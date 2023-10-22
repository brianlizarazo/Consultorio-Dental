const sweetAlert = (text, confirmButtonText, confirmButtonColor, evento) => {
  Swal.fire({
    icon: "question",
    titleText: "¿Está seguro?",
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

const enlacesDespedir = document.querySelectorAll(".despedir-doctor");

enlacesDespedir.forEach((enlace) => {
  enlace.addEventListener("click", (evento) => {
    evento.preventDefault();
    sweetAlert("¿Quiere eliminar a este doctor de la base de datos?", "Despedir", "#dc3545", evento);
  });
});
