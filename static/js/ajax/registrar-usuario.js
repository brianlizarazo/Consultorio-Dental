$(document).ready(function () {
  $("#form-signup-login").on("submit", function (evento) {
    evento.preventDefault();
    $.ajax({
      type: "POST",
      url: "registrar-usuario",
      data: {
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        username: $("#username").val(),
        password: $("#password").val(),
        email: $("#email").val(),
        phone: $("#phone").val()
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
            window.location = "/";
          },
          allowOutsideClick: () => false,
          allowEscapeKey: () => false,
        });
      }
    });
  });
});
