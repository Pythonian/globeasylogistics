(function ($) {
  "use strict";

  // Offcanvas menu
  $(".menu-trigger").on("click", function () {
    $(".extra-info,.offcanvas-overly").addClass("active");
    return false;
  });
  $(".menu-close,.offcanvas-overly").on("click", function () {
    $(".extra-info,.offcanvas-overly").removeClass("active");
  });

  // Metis Menu 

  $("#mobile-menu").metisMenu();

  $('#hamburger').on('click', function () {
    $('.mobile-nav').addClass('show');
    $('.overlay').addClass('active');
  });

  $('.close-nav').on('click', function () {
    $('.mobile-nav').removeClass('show');
    $('.overlay').removeClass('active');
  });

  $(".overlay").on("click", function () {
    $(".mobile-nav").removeClass("show");
    $('.overlay').removeClass('active');
  });


  // Sticky Header Js

  var windowOn = $(window);

  windowOn.on('scroll', function () {
    var scroll = windowOn.scrollTop();
    if (scroll < 400) {
      $("#header-sticky").removeClass("header-sticky");
    } else {
      $("#header-sticky").addClass("header-sticky");
    }
  });

  // Active & Remove Class

  $(".sub-menu ul li").on("click", function () {
    $(".sub-menu").removeAttribute("style");
    $(this).addClass("active");
  });

  $("a.nav-link").on("mouseover", function () {
    $("a.nav-link").removeClass("active");
    $(this).addClass("active");
  });

  //Hide Loading Box (Preloader)
  function handlePreloader() {
    if ($(".preloader").length) {
      $(".preloader").delay(200).fadeOut(500);
    }
  }

  $(window).on("load", function () {
    handlePreloader();
  });

})(window.jQuery);
