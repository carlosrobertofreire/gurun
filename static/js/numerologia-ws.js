jQuery(document).ready(function(){ 
    jQuery('input[type=text]').first().focus();
    jQuery('input[type=text]').keypress(function (e) {
        var allowedChars = new RegExp("^[a-zA-ZÀ-ú\\s]+$");
        var str = String.fromCharCode(!e.charCode ? e.which : e.charCode);
        if (allowedChars.test(str)) {
            return true;
        }
        e.preventDefault();
        return false;		    
    }).keyup(function() {
        var forbiddenChars = new RegExp("[^a-zA-ZÀ-ú\\s]", 'g');
        if (forbiddenChars.test(jQuery(this).val())) {
            jQuery(this).val(jQuery(this).val().replace(forbiddenChars, ''));
        }
        this.value = this.value.toLocaleUpperCase();
        if (jQuery(this).val() != '') { 
            jQuery('button[type=submit]').removeAttr('disabled');
        } else{                    
            jQuery('button[type=submit]').attr('disabled','disabled');
        }
    });
});
