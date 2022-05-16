function make_select(id, options, selected) {
	var select = document.createElement("select");
   	select.id = id;
	var version_found = false
	for (const [key, value] of Object.entries(options)) {
		var select_item = key === selected
		var option = new Option(value.name, key, select_item, select_item);
		select.add(option);
		if (select_item) {
			version_found = true
		}
	}
	if (!version_found) {
		var option = new Option(selected, selected, true, true);
		select.add(option);
	}
	return select;
}

function is_absolute(url) {
    var isAbsolute = new RegExp('^([a-z]+://|/)', 'i');
    return isAbsolute.test(url);
}

function make_url(url) {
    return is_absolute(url) ? url : base_url + '/../' + url;
}

$(document).ready(function(){
	if (multiversion) {
	    var url = make_url(multiversion.versions_url ? multiversion.versions_url : 'multiversion.json');
		$.getJSON(url).done(function(versions) {
			var place = $('.wy-side-nav-search').children().first();
			var select = make_select('multiversion-selector', versions, multiversion.current_version);
			$(select).attr('class', 'form-control form-select form-select-sm');
			var obj = $(select).insertAfter(place);
			obj.change(function() {
				var url = $(location).attr('href');
				var newVersion = $(this).val();
				var repRegex = new RegExp(multiversion.current_version,'g');
				url = url.replace(repRegex, newVersion);
				$(location).attr('href', url);
			});
		});
	}
})
