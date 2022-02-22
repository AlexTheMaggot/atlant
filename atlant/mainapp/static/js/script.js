
// Наведение локализации
$('.lang li').hover(function(){
    $(this).toggleClass('active-lang');
});
$('.rus_lang').click(function(){
  $('.rus_lang').addClass('active-lang')
  $('.uzb_lang').removeClass('active-lang')
})
$('.uzb_lang').click(function(){
  $('.uzb_lang').addClass('active-lang')
  $('.rus_lang').removeClass('active-lang')
})
// Скрипты хедера
$('.nav__link__elem').find('ul').hide();
let $mobile_sub_menu = $('.mobile-category-nav ul li').children('ul')
$mobile_sub_menu.hide()
$mobile_sub_menu.parent('li').prepend('<button class="open-mobile-nav"><span></span><span></span></button>')

if($(window).width() <= 992){
  let menu_button = document.querySelector('.menu_button');
  let mobile_nav_list = document.querySelector('.mobile_nav_list');
  $('.open_catalog_button').click(function(){
    $('.mobile_menu').addClass('toggle_mobile_menu')
    $('body').addClass('body_no_scroll')
  })
  $('.open_search_button').click(function(){
    $('.mobile_menu').addClass('toggle_mobile_menu')
    $('#search_input_form').focus()
    $('body').addClass('body_no_scroll')
  })
  $('.mobile_clouse_button button').click(function(){
    $('.mobile_menu').removeClass('toggle_mobile_menu')
    $('body').removeClass('body_no_scroll')
  })
  var postion = $('.mobile_catalog').offset().top,
      height = $('.mobile_catalog').height();
    $(document).on('scroll', function (){
      var scroll = $(document).scrollTop();
      if(scroll  > postion) {
        $('.mobile_catalog').css('box-shadow','0 10px 10px 0 rgba(0, 0, 0, .2)')
        }else {
          $('.mobile_catalog').css('box-shadow','none')
        }
    })
  menu_button.onclick = () => {
    menu_button.classList.toggle('active');
    mobile_nav_list.classList.toggle('toggle_menu');
  }
  $('.mobile_menu').prepend('')
  $('.menu-clouse').hide();

  $('.menu-clouse').click(function(){
    $('.mobile_menu').fadeOut(300);
    $('body').removeClass('block-scroll');
  });
  $('.open-mobile-nav').on('click', function() {
    if ($(this).parent().children('ul').css('display') == 'none') {
      $(this).addClass('open')
      $(this).parent().children('ul').slideDown(400)
      $(this).parent().addClass('open')
      $(this).find('span').css('transform','rotate(0deg)')
    }
    else {
      $(this).removeClass('open');
      $(this).parent().children('ul').slideUp(400);
      $(this).parent().removeClass('open')
      $(this).find('span:last-child').css('transform','rotate(90deg)')
    }
  });
  $('.mobile_all-product ul').hide()
  $('.open-cat-list').click(function(){
    $('.open-cat-list').toggleClass('open')
    $('.mobile_all-product-link').toggleClass('open')
    $('.mobile_all-product ul').slideToggle(300);
  })
  $('.mobile_rus_lang').click(function(){
    $('.mobile_rus_lang').addClass('active')
    $('.mobile_uzb_lang').removeClass('active')
  })
  $('.mobile_uzb_lang').click(function(){
    $('.mobile_uzb_lang').addClass('active')
    $('.mobile_rus_lang').removeClass('active')
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
  // autoplay: {
  //         delay: 2500,
  //         disableOnInteraction: false,
  //       },
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

let slide = document.createElement('div');

slide.setAttribute('class','swiper-slide reviews-slide')
// let items = document.querySelectorAll('.rewiew-slider-item');

// for(let item of items){
//   slide.append(item)
// }






// поле поиска
// $(".seacrh_btn").click(function(){
//   $(".input_search_index").toggleClass("active").focus;
//   $(".input_search_index").val("");
// });
let search_button = document.querySelector('.seacrh_btn');
let input_search_index = document.querySelector('.form_search');
// let search_form = document.querySelector('.search form');

let enter_search = document.createElement('button');
// let icon_search = document.createElement('i');

// icon_search.classList.add('fas');
// icon_search.classList.add('fa-search');
// enter_search.append(icon_search);
// enter_search.classList.add('enter_search');
// search_form.append(enter_search);

search_button.onclick = () => {
  input_search_index.classList.toggle('active')
  search_button.classList.toggle('active')
}