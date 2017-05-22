var production_url = 'http://127.0.0.1:8000/';
var deployment_url = 'http://112.74.48.237/';
var post_url = production_url;

save_answer_url = post_url + 'save_answer/';

// This loads date picker .and calendar image
$( function() {
    $( ".datepicker" ).datepicker({
        showOn: "button",
        buttonImage: $('.calendar_image_url').attr('value'),//"{% static 'portals/images/calendar.png' %}",
        buttonImageOnly: true,
        buttonText: "Select date"
    });
    $( ".datepicker" ).datepicker( "option", "dateFormat", "DD" );
});//end date picker calendar image.

$('.basicExample').timepicker();

// When Date Picker Changes Show Date Selected
    $('#datepicker').change(function() {
        $( ".spanDate" ).html($( "#datepicker" ).val() + 's');
    });//end change

    $('#datepicker2').change(function() {
        $( ".spanDate2" ).html($( "#datepicker2" ).val() + 's');
    });//end change

    $('#datepicker3').change(function() {
        $( ".spanDate3" ).html($( "#datepicker3" ).val() + 's');
    });
// When Date Picker Changes Show Date Selected End

function Register() {
    $('.ajaxProgress').show();
    $.ajax({
        type: "POST",
        url: $('.register_form input.url').val(),
        dataType: "json",
        async: true,
        data: {
            csrfmiddlewaretoken: $('.register_form input[name=csrfmiddlewaretoken]').val(),
            username: $('#id_username').val(),
            email: $('#id_email').val(),
            password: $('#id_password').val(),
        },//data close

        success: function(json) {
            console.log(json.message, json.username, json.password);
            $('ajaxProgress').hide();
            $('.register_form').toggle('');
            $('.student_form').toggle('');
        }


    });//ajax close
}//function Register close


function CreateStudent() {
    $('.ajaxProgress').show();
    $.ajax({
        type: "POST",
        url: $('.student_form input.url').val(),
        dataType: "json",
        async: true,
        data: {
            csrfmiddlewaretoken: $('.student_form input[name=csrfmiddlewaretoken]').val(),
            name: $('#id_name').val(),
            is_adult: $('input[name=is_adult]:checked').val(),
            age: $('#id_age').val(),
        },//data close

        success: function(json) {
            console.log( json.name, json.username, json.result);
            $('ajaxProgress').hide();
            $('.student_form').toggle('');
            $('.class_form').toggle('');
        }


    });//ajax close
}//function Register close

function CreateClass() {
    $('.ajaxProgress').show();
    $.ajax({
        type: "POST",
        url: $('.class_form input.url').val(),
        dataType: "json",
        async: true,
        data: {
            csrfmiddlewaretoken: $('.class_form input[name=csrfmiddlewaretoken]').val(),
            days_a_week: $('input[name=days_of_class]:checked').val(),
            
            day1: $('#datepicker').val(),
            day1_from: $('#timepicker1_from').val(),
            day1_to: $('#timepicker1_to').val(),

            day2: $('#datepicker2').val(),
            day2_from: $('#timepicker2_from').val(),
            day2_to: $('#timepicker2_to').val(),

            day3: $('#datepicker3').val(),
            day3_from: $('#timepicker3_from').val(),
            day3_to: $('#timepicker3_to').val(),

        },//data close

        success: function(json) {
            console.log(json.age, json.name, json.is_adult);
            $('ajaxProgress').hide();
            $('.register_form').toggle('');
            $('.student_form').toggle('');
            window.location.replace("http://127.0.0.1:8000/portals/");

        }


    });//ajax close
}//function Create Class close

// changes age visibility on is_adult change
$('.age_input input').change(function() {
    if ($(this).attr('id') === 'under_18') {
        $('#id_age').removeClass('age_hidden');
    } else {
        $('#id_age').addClass('age_hidden');
        $('#id_age').val('');
    }
});//end change

// changes calendar visibility days change
$('.days_of_class input').change(function() {
    if ($(this).attr('id') === '1day') {
    	$('.day1').show('');
        $('.day2').hide('');
        $('.day3').hide('');
    } else if ($(this).attr('id') === '2days') {
    	$('.day1').show('');
    	$('.day2').show('');
        $('.day3').hide('');
    }

    else {
        $('.day1').show('');
    	$('.day2').show('');
        $('.day3').show('');
    }
});//end change

// On Click Load Login
function loadLogin() {
    console.log("loading login");
    $( "#loadLogin .modal-body" ).load( "login/");
}


// On Click Load Register
function loadRegister() {
    $( "#loadRegister .modal-body" ).load( "register/");
}

// On Click Load Register

function loadChangeUserPic() {
    $.ajax({
        type: "GET",
        url: 'change_user_image/',
        dataType: "html",

        success: function(data) {
            console.log('WORKED! Success!!');
            $( "#load_change_user_pic .modal-body" ).html(data);
        }


    });//ajax close
}//function load Change Class close


//save answer
function saveAnswer(answer_id, exam_paper_id, question_id) {
    console.log("Save answer entered!");
    var answer_url_input = '#answer' + answer_id;
    var url = $('#save_answer_url').val();
    var csrftoken = $('#save_answer_span input[name=csrfmiddlewaretoken]').val();



    console.log( url, answer_url_input, csrftoken, answer_id, exam_paper_id);
    $.ajax({
        type: "POST",
        // url: url,
        url: save_answer_url,
        dataType: "json",
        async: true,
        data: {
            csrfmiddlewaretoken: $('#save_answer_span input[name=csrfmiddlewaretoken]').val(),
            answer_id: answer_id,
            exam_paper_id: exam_paper_id,

        },//data close

        success: function(json) {
            console.log(json.the_status);
            console.log("Shoudl say great!!!");
            $( "#saved_answer" + question_id ).html(json.saved_answer);
            var specific_answer_selector_string = "#question" + question_id + " #answer" + json.saved_answer_id;
            var all_answers_selector_string = "#question" + question_id + " .an_answer";
            var all_answers = $(all_answers_selector_string);
            
            // Remove all success classes
            all_answers.removeClass('label label-success');

            // Add Success class to clicked answer
            $( specific_answer_selector_string ).addClass('label label-success');
            console.log(selector_string);
            console.log(json.saved_answer);
            console.log(json.error);
        },

        error: function(json) {
            console.log(json);
            console.log(json.error);
        }


    });//ajax close
}//function Create Class close

// Mark Video Watched
function mark_video_watched(video_id) {
    vid_url = post_url + "mark_video_watched/" + video_id +"/";
    console.log(vid_url);
    $.ajax({
        type: "GET",
        url: vid_url,
        dataType: "html",
        async: true,

        success: function(data) {
            console.log(data, typeof data);
            data = JSON.parse(data);
            console.log(data.watched, typeof data);


            // If video is watched switch checkmark icon class to show watched
            // else switch to show not watched
            if (data.watched === true) {
                console.log("True statement entered");
            } else if (data.watched === false) {
                console.log("False statement entered");
            }


            // Update Progress Bar
            $('.percentage_class').html(data.percentage);
            $('.progress-bar.progress-bar-info').css('width', data.percentage + '%');

        }//success close


    });//ajax close
}//function mark Video close

// Load Video
function loadVideo(video_id) {
    vid_url = post_url + "video/" + video_id +"/";
    console.log(vid_url);
    $.ajax({
        type: "GET",
        url: vid_url,
        dataType: "html",
        async: true,

        success: function(data) {
            $( "#video" + video_id + " .modal-body" ).html(data);
            console.log(vid_url);
        },//success close

        error: function(json) {
            console.log(json);
            console.log(json.error);
            console.log("An error occured");
        },


    });//ajax close
}//function loadVideo close

// Load Video
// function loadVideo(video_id) {
//     $( "#video" + video_id + " .modal-body" ).load( "video/" + video_id +"/");


// }

$('.myModal').modal({
    show: false
}).on('hidden.bs.modal', function(){
    $(this).find('video')[0].pause();
});