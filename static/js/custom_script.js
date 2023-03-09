jQuery(document).ready(function($) {
    "use strict";
	//Banner
    if ($('#home-slider').length) {
        $('#home-slider').owlCarousel({
            loop: true,
            dots: false,
            nav: true,
            items: 1,
        });
    }
	
   //POST SLIDER
    if ($('.post-slider').length) {
        $('.post-slider').owlCarousel({
            loop: false,
            dots: false,
            nav: true,
            items: 1,
        });
    }
	
	
	//bxslider
	if ($('.bxslider').length) {
	$('.bxslider').bxSlider({
  	pagerCustom: '#bx-pager'
		});
	}
	
	 //EVENT TIMER
    if ($('.countdown236').length) {
        var austDay = new Date();
        austDay = new Date(2021, 11 - 1, 11, 15, 35, 0);
        $('.countdown236').countdown({
            until: austDay,
        });
        $('#year').text(austDay.getFullYear());
    }

	
	//AUDIO
	if ($('audio').length) {
	  $('audio').audioPlayer();
	}
    //Function End
});
// jQuery (مستند). true ، dots: false ، nav: true ، items: 1،})؛} // POST SLIDER if ($ ('. post-slider'). length) {$ ('. post-slider'). owlCarousel ({ loop: false، dots: false، nav: true، items: 1،})؛} // bxslider if ($ ('. bxslider'). length) {$ ('. bxslider'). bxSlider ({pagerCustom: ' # bx-pager '})؛} // EVENT TIMER if ($ ('. countdown236 '). length) {var austDay = new Date ()؛ austDay = new Date (2021، 11-1، 11، 15، 35 ، 0)؛ $ ('. countdown236'). countdown ({until: austDay،})؛ $ ('# year'). text (austDay.getFullYear ())؛} // AUDIO if ($ ('audio') ) .length) {$ ('audio'). audioPlayer ()؛} // Function End})؛