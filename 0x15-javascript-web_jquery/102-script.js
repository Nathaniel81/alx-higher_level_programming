$(document).ready(function () {
	$('#btn_translate').click(() => {
		lang = $('#language_code').val();
		$.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`,(data, status) => {
			(data, status) => {
				$('#hello').text(data.hello);
			}
		});
	});
});		
