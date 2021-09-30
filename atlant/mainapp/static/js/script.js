// Наведение локализации
$('.lang li').hover(function(){
    $(this).toggleClass('active-lang');
});
$('.lang li').click(function(){
    $(this).addClass('active-lang');
});
// Скрипты хедера
$('.nav__link__elem').find('ul').hide();
let $mobile_sub_menu = $('.mobile-category-nav ul li').children('ul')
$mobile_sub_menu.parent('li').append('<button class="open-mobile-nav"><i class="fas fa-chevron-right"></i></button>')
if($(window).width() <= 992){
  $('.mobile_menu').prepend('')
  $('.menu-clouse').hide();
  $('.mobile-button button').click(function(){
    $('.overlay').slideDown(500);
    $('.mobile_menu').fadeIn(900);
    $('.mobile-button button').hide();
    $('.menu-clouse').fadeIn(810);
    $('body').addClass('block-scroll');
  });
  $('.menu-clouse').click(function(){
    $('.mobile_menu').fadeOut(300);
    $('.overlay').fadeOut(400);
    $('.mobile-button button').show(100);
    $('body').removeClass('block-scroll');
  });
  $('.overlay').click(function(){
    $('.mobile_menu').fadeOut(300);
    $('.overlay').fadeOut(400);
    $('.mobile-button button').show(100);
    $('body').removeClass('block-scroll');
  });
  $('.open-mobile-nav').on('click', function() {
    if ($(this).parent().children('ul').css('display') == 'none') {
      $(this).html('<i class="fas fa-chevron-down"></i>')
      $(this).parent().children('ul').slideDown(400)
    }
    else {
      $(this).html('<i class="fas fa-chevron-right"></i>');
      $(this).parent().children('ul').slideUp(400);
    }
  });
  $('.open-cat-list').click(function(){
    $('.mobile_all-product ul').slideToggle(300);
  })
} else{
  $('.nav__link__elem a').mouseenter(function (e) {
    $(this).parent().children('ul').fadeIn(400);
    });
    
    $('.nav__link__elem').mouseleave(function (e) {
      $(this).find('ul').fadeOut(400);
    });
};
$('.all-category-link').click(function() {
  $('.all-category').toggleClass('open-list')
})



// Анимация цифр на главной странице
if($('body').find('div').hasClass('company-text')){
  var show = true;
  var countbox = ".benefits__inner";
  $(window).on("scroll load resize", function () {
      if (!show) return false; // Отменяем показ анимации, если она уже была выполнена
      var w_top = $(window).scrollTop(); // Количество пикселей на которое была прокручена страница
      var e_top = $(countbox).offset().top; // Расстояние от блока со счетчиками до верха всего документа
      var w_height = $(window).height(); // Высота окна браузера
      var d_height = $(document).height(); // Высота всего документа
      var e_height = $(countbox).outerHeight(); // Полная высота блока со счетчиками
      if (w_top + 500 >= e_top || w_height + w_top == d_height || e_height + e_top < w_height) {
          $('.benefits__number').css('opacity', '1');
          $('.benefits__number').spincrement({
              thousandSeparator: "",
              duration: 1200
          });

          show = false;
      }
  });
} else{

}








$('.set-bg').each(function () {
         var bg = $(this).data('setbg');
         $(this).css('background-image', 'url(' + bg + ')');
     });


$('.bg-pstn').each(function () {
         var bg = $(this).data('bgpstn');
         $(this).css('background-image', 'url(' + bg + ')');
     });
$('.bg-center').each(function () {
         var bg = $(this).data('bgcenter');
         $(this).css('background-image', 'url(' + bg + ')');
     });
$('.bg-right').each(function () {
         var bg = $(this).data('bg-right');
         $(this).css('background-image', 'url(' + bg + ')');
     });






const swiper = new Swiper('.swiper-container', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  autoplay: {
          delay: 2500,
          disableOnInteraction: false,
        },
  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
});







$(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    items: 4,
    dots: false,
    nav: true,
    smartSpeed: 1200,
    autoHeight: false,
    autoPlay: true,
    responsive: {

        0: {
            items: 2,
        },

        480: {
            items: 3,
        },

        768: {
            items: 4,
        },

        992: {
            items: 4,
        }
    }
});

$(document).ready(function(){
  $('.gallery_button').click(function(){
    event.preventDefault();
    var $elem = $(this).find('img').clone();
    $('.zoom_img').html($elem);
    $('.zoom_img').find('img').loupe();
  })
  $('.zoom_img').find('img').loupe();
})


$(document).ready(function(){
  $('.gallery_button').click(function(){
    event.preventDefault();
    var $elem = $(this).find('img').clone();
    $('.zoom_img').html($elem);
    $('.zoom_img').find('img').loupe();
  })
  $('.zoom_img').find('img').loupe();
})





if($('body').find('div').hasClass('tabs')){
  const tabsBtn   = document.querySelectorAll(".tabs__nav-btn");
  const tabsItems = document.querySelectorAll(".tabs__item");

  tabsBtn.forEach(onTabClick);

  function onTabClick(item) {
      item.addEventListener("click", function() {
        let currentBtn = item;
        let tabId = currentBtn.getAttribute("data-tab");
        let currentTab = document.querySelector(tabId);

        if( ! currentBtn.classList.contains('active') ) {
            tabsBtn.forEach(function(item) {
                item.classList.remove('active');
            });
    
            tabsItems.forEach(function(item) {
                item.classList.remove('active');
            });
    
            currentBtn.classList.add('active');
            currentTab.classList.add('active');
        }
    });
}
document.querySelector('.tabs__nav-btn').click();
} else{

}


function notification(html) {
  $('.toast').toast('show')
  $('.toast-body').html(html)
}