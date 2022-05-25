 var $myCarousel = $('#carouselExampleIndicators');

Initialize ;carousel
$myCarousel.carousel();

var $firstAnimatingElems = $myCarousel.find('.carousel-item:first')
.find("[data-animation ^= 'animated']");  
doAnimations($firstAnimatingElems);