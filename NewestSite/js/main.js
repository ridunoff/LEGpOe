;(function () {

	'use strict';



	// iPad and iPod detection
	var isiPad = function(){
		return (navigator.platform.indexOf("iPad") != -1);
	};

	var isiPhone = function(){
	    return (
			(navigator.platform.indexOf("iPhone") != -1) ||
			(navigator.platform.indexOf("iPod") != -1)
	    );
	};

	// Parallax
	var parallax = function() {
		$(window).stellar();
	};



	// Burger Menu
	var burgerMenu = function() {

		$('body').on('click', '.js-fh5co-nav-toggle', function(event){

			event.preventDefault();

			if ( $('#navbar').is(':visible') ) {
				$(this).removeClass('active');
			} else {
				$(this).addClass('active');
			}

		});

	};


	// Page Nav
	var clickMenu = function() {

		$('#navbar a:not([class="external"])').click(function(event){
			var section = $(this).data('nav-section'),
				navbar = $('#navbar');

				if ( $('[data-section="' + section + '"]').length ) {
			    	$('html, body').animate({
			        	scrollTop: $('[data-section="' + section + '"]').offset().top - 55
			    	}, 500);
			   }

		    if ( navbar.is(':visible')) {
		    	navbar.removeClass('in');
		    	navbar.attr('aria-expanded', 'false');
		    	$('.js-fh5co-nav-toggle').removeClass('active');
		    }

		    event.preventDefault();
		    return false;
		});


	};

	// Reflect scrolling in navigation
	var navActive = function(section) {

		var $el = $('#navbar > ul');
		$el.find('li').removeClass('active');
		$el.each(function(){
			$(this).find('a[data-nav-section="'+section+'"]').closest('li').addClass('active');
		});

	};

	var navigationSection = function() {

		var $section = $('section[data-section]');

		$section.waypoint(function(direction) {

		  	if (direction === 'down') {
		    	navActive($(this.element).data('section'));
		  	}
		}, {
	  		offset: '150px'
		});

		$section.waypoint(function(direction) {
		  	if (direction === 'up') {
		    	navActive($(this.element).data('section'));
		  	}
		}, {
		  	offset: function() { return -$(this.element).height() + 155; }
		});

	};

	// Window Scroll
	var windowScroll = function() {
		var lastScrollTop = 0;

		$(window).scroll(function(event){

		   	var header = $('#fh5co-header'),
				scrlTop = $(this).scrollTop();

			if ( scrlTop > 500 && scrlTop <= 2000 ) {
				header.addClass('navbar-fixed-top fh5co-animated slideInDown');
			} else if ( scrlTop <= 500) {
				if ( header.hasClass('navbar-fixed-top') ) {
					header.addClass('navbar-fixed-top fh5co-animated slideOutUp');
					setTimeout(function(){
						header.removeClass('navbar-fixed-top fh5co-animated slideInDown slideOutUp');
					}, 100 );
				}
			}

		});
	};

	var counter = function() {
		$('.js-counter').countTo({
			 formatter: function (value, options) {
	      return value.toFixed(options.decimals);
	    },
		});
	};

	var counterWayPoint = function() {
		if ($('#fh5co-counter-section').length > 0 ) {
			$('#fh5co-counter-section').waypoint( function( direction ) {

				if( direction === 'down' && !$(this.element).hasClass('animated') ) {
					setTimeout( counter , 400);
					$(this.element).addClass('animated');
				}
			} , { offset: '90%' } );
		}
	};

	var contentWayPoint = function() {
		var i = 0;
		$('.animate-box').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('animated-fast') ) {

				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function(){

					$('body .animate-box.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							var effect = el.data('animate-effect');
							if ( effect === 'fadeIn') {
								el.addClass('fadeIn animated-fast');
							} else if ( effect === 'fadeInLeft') {
								el.addClass('fadeInLeft animated-fast');
							} else if ( effect === 'fadeInRight') {
								el.addClass('fadeInRight animated-fast');
							} else {
								el.addClass('fadeInUp animated-fast');
							}

							el.removeClass('item-animate');
						},  k * 50, 'easeInOutExpo' );
					});

				}, 50);

			}

		} , { offset: '85%' } );
	};



	// Get the modal 1
	var modal = document.getElementById('myModal');
	// Get the button that opens the modal 1
	var btn = document.getElementById("myBtn");

	// Get the <span> element that closes the modal
	var span = document.getElementById("close");

	// When the user clicks on the button, open the modal
	btn.onclick = function() {
	    modal.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span.onclick = function() {
	    modal.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
	    if (event.target == modal) {
	        modal.style.display = "none";
	    }
	}

	// Get the modal 2
	var modal2 = document.getElementById('myModal2');
	// Get the button that opens the modal 1
	var btn2 = document.getElementById("myBtn2");

	// Get the <span> element that closes the modal
	var span2 = document.getElementById("close2");

	// When the user clicks on the button, open the modal
	btn2.onclick = function() {
			modal2.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span2.onclick = function() {
			modal2.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
			if (event.target == modal2) {
					modal2.style.display = "none";
			}
	}

	// Get the modal 3
	var modal3 = document.getElementById('myModal3');
	// Get the button that opens the modal 3
	var btn3 = document.getElementById("myBtn3");

	// Get the <span> element that closes the modal
	var span3 = document.getElementById("close3");

	// When the user clicks on the button, open the modal
	btn3.onclick = function() {
			modal3.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span3.onclick = function() {
			modal3.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
			if (event.target == modal3) {
					modal3.style.display = "none";
			}
	}

	// Get the modal 4
	var modal4 = document.getElementById('myModal4');
	// Get the button that opens the modal 4
	var btn4 = document.getElementById("myBtn4");

	// Get the <span> element that closes the modal
	var span4 = document.getElementById("close4");

	// When the user clicks on the button, open the modal
	btn4.onclick = function() {
			modal4.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span4.onclick = function() {
			modal4.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
			if (event.target == modal4) {
					modal4.style.display = "none";
			}
	}

	// Get the modal 5
	var modal5 = document.getElementById('myModal5');
	// Get the button that opens the modal 5
	var btn5 = document.getElementById("myBtn5");

	// Get the <span> element that closes the modal
	var span5 = document.getElementById("close5");

	// When the user clicks on the button, open the modal
	btn5.onclick = function() {
			modal5.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span5.onclick = function() {
			modal5.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
			if (event.target == modal5) {
					modal5.style.display = "none";
			}
	}
	// Get the modal 6
	var modal6 = document.getElementById('myModal6');
	// Get the button that opens the modal 3
	var btn6 = document.getElementById("myBtn6");

	// Get the <span> element that closes the modal
	var span6 = document.getElementById("close6");

	// When the user clicks on the button, open the modal
	btn6.onclick = function() {
			modal6.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span6.onclick = function() {
			modal6.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
			if (event.target == modal6) {
					modal6.style.display = "none";
			}
	}

	// Get the modal 7
	var modal7 = document.getElementById('myModal7');
	// Get the button that opens the modal 3
	var btn7 = document.getElementById("myBtn7");

	// Get the <span> element that closes the modal
	var span7 = document.getElementById("close7");

	// When the user clicks on the button, open the modal
	btn7.onclick = function() {
			modal7.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span7.onclick = function() {
			modal7.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
			if (event.target == modal7) {
					modal7.style.display = "none";
			}
	}

	// Get the modal 8
	var modal8 = document.getElementById('myModal8');
	// Get the button that opens the modal 8
	var btn8 = document.getElementById("myBtn8");

	// Get the <span> element that closes the modal
	var span8 = document.getElementById("close8");

	// When the user clicks on the button, open the modal
	btn8.onclick = function() {
			modal8.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span8.onclick = function() {
			modal8.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
			if (event.target == modal8) {
					modal8.style.display = "none";
			}
	}

	// Get the modal 9
	var modal9 = document.getElementById('myModal9');
	// Get the button that opens the modal 3
	var btn9 = document.getElementById("myBtn9");

	// Get the <span> element that closes the modal
	var span9 = document.getElementById("close9");

	// When the user clicks on the button, open the modal
	btn9.onclick = function() {
			modal9.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span9.onclick = function() {
			modal9.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
			if (event.target == modal9) {
					modal9.style.display = "none";
			}
	}

	// Get the modal 10
	var modal10 = document.getElementById('myModal10');
	// Get the button that opens the modal 3
	var btn10 = document.getElementById("myBtn10");

	// Get the <span> element that closes the modal
	var span10 = document.getElementById("close10");

	// When the user clicks on the button, open the modal
	btn10.onclick = function() {
			modal10.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span10.onclick = function() {
			modal10.style.display = "none";
	}

	// Get the modal 11
	var modal11 = document.getElementById('myModal11');
	// Get the button that opens the modal 3
	var btn11 = document.getElementById("myBtn11");

	// Get the <span> element that closes the modal
	var span11 = document.getElementById("close11");

	// When the user clicks on the button, open the modal
	btn11.onclick = function() {
			modal11.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span11.onclick = function() {
			modal11.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
			if (event.target == modal11) {
					modal11.style.display = "none";
			}
	}

	// Document on load.
	$(function(){

		parallax();
		burgerMenu();
		clickMenu();
		windowScroll();
		navigationSection();
		counterWayPoint();
		contentWayPoint();

	});


}());
