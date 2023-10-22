$(document).ready(function () {
  $("#form-actualizar-doctor").on("submit", function (evento) {
    evento.preventDefault();
    telefonos = [];
    $('input[name="telefono"]').each(function () {
      telefonos.push($(this).val());
    });
    emails = [];
    $('input[name="email"]').each(function () {
      emails.push($(this).val());
    });
    $.ajax({
      type: "POST",
      url: "/cambiar-doctor",
      data: {
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        ciDoctor: $("#ci-doctor").val(),
        nombres: $("#nombres").val(),
        apellidos: $("#apellidos").val(),
        direccion: $("#direccion").val(),
        especialidad: $("#especialidad").val(),
        telefonos: telefonos.toString(),
        emails: emails.toString()
      }
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
            window.location = "/administrar-doctores";
          },
          allowOutsideClick: () => false,
          allowEscapeKey: () => false,
        });
      }
    });
  });
});