$(document).ready(function () {
  $(".reserve-button").on("click", function () {
    $(".modal").removeClass("hidden");
  });
  $(".modal__close").on("click", function () {
    $(".modal").addClass("hidden");
  });
  $(".aside__burger").on("click", function () {
    $(".burger").removeClass("hidden");
  });
  $(".burger__close").on("click", function () {
    $(".burger").addClass("hidden");
  });
});
