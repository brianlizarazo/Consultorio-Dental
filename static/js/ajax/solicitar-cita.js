$(document).ready(function () {
  $("#form-solicitar-cita").on("submit", function (evento) {
    evento.preventDefault();
    let primeraVez;
    if ($('input:radio[name="primera-vez"]:checked').val() === undefined) {
      primeraVez = "False";
    } else {
      primeraVez = $('input:radio[name="primera-vez"]:checked').val();
    }
    telefonos = [];
    $('input[name="telefono"]').each(function () {
      telefonos.push($(this).val());
    });
    emails = [];
    $('input[name="email"]').each(function () {
      emails.push($(this).val());
    });
    let tieneParentesco;
    if ($('input:radio[name="tiene-parentesco"]:checked').val() === undefined) {
      tieneParentesco = "False";
    } else {
      tieneParentesco = $('input:radio[name="tiene-parentesco"]:checked').val();
    }
    $.ajax({
      type: "POST",
      url: "procesar-cita",
      data: {
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        ciCliente: $("#nci-cliente").val(),
        nacionalidadCliente: $("#nacionalidad-cliente").val(),
        fechaCita: $("#fecha-cita").val(),
        horaCita: $("#hora-cita").val(),
        motivoConsulta: $("#motivo-consulta").val(),
        sintomas: $('#sintomas').val().toString(),
        doctorCita: $('#doctor-cita').val(),
        urgencia: $("#urgencia").val(),
        detalles: $("#detalles").val(),
        primeraVez: primeraVez,
        nombres: $('#nombres').val(),
        apellidos: $('#apellidos').val(),
        fechaNacimiento: $('#fecha-de-nacimiento').val(),
        sexo: $('#sexo').val(),
        direccion: $('#direccion').val(),
        necesidadEspecial: $('#necesidad-especial').val(),
        telefonos: telefonos.toString(),
        emails: emails.toString(),
        tieneParentesco: tieneParentesco,
        ciPariente: $('#nci-pariente').val(),
        nacionalidadPariente: $('#nacionalidad-pariente').val(),
        parentesco : $('#parentesco').val()
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
          allowEscapeKey: () => false
        });
      }
      else {
        Swal.fire({
          titleText: respuesta.title,
          text: respuesta.success,
          icon: respuesta.icon,
          confirmButtonText: respuesta.confirmButton,
          showLoaderOnConfirm: true,
          preConfirm: () => {
            window.location = '/';
          },
          allowOutsideClick: () => false,
          allowEscapeKey: () => false
        });
      }
    });
  });
});
