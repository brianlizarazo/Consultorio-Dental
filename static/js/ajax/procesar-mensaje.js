$(document).ready(function () {
  $("#form-procesar-mensaje").on("submit", function (evento) {
    evento.preventDefault();
    $.ajax({
      type: "POST",
      url: "procesar-mensaje",
      data: {
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        nombre: $("#nombre").val(),
        apellido: $("#apellido").val(),
        email: $("#email").val(),
        phone: $("#phone").val(),
        mensaje: $("#mensaje").val(),
      },
    }).done(function (respuesta) {
      if (respuesta.error) {
        $(respuesta.id).focus();
        Swal.fire({
          titleText: respuesta.title,
          text: respuesta.error,
          icon: respuesta.icon,
          confirmButtonText: respuesta.confirmButton,
          allowOutsideClick: () => false,
          allowEscapeKey: () => false,
        });
      } else {
        Swal.fire({
          titleText: respuesta.title,
          text: respuesta.success,
          icon: respuesta.icon,
          confirmButtonText: respuesta.confirmButton,
          showLoaderOnConfirm: true,
          preConfirm: () => {
            window.location = "/contactos";
          },
          allowOutsideClick: () => false,
          allowEscapeKey: () => false,
        });
      }
    });
  });
});
