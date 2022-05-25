/**
 * You can write your JS code here, DO NOT touch the default style file
 * because it will make it harder for you to update.
 *
 * @format
 */

"use strict";

$(document).ready(function () {
  $("form.ajax").submit(function (event) {
    event.preventDefault();
    swal({
      title: "Proccessing...!",
      text: "Please wait",
      icon: "info",
      button: false,
    });

    let $this = $(this);
    var url = $this.attr("action");
    var method = $this.attr("method");
    // var data = $($this).serialize();

    $.ajax({
      type: method,
      url: url,
      dataType: "json",
      contentType: false,
      processData: false,
      data: new FormData(this),

      success: function (data) {
        if (data["status"] == "true") {
          if (data["swal_icon"]) {
            var swal_icon = data["swal_icon"];
          } else {
            var swal_icon = "success";
          }

          if (data["swal_title"]) {
            var swal_title = data["swal_title"];
          } else {
            var swal_title = "Success !";
          }

          if (data["swal_text"]) {
            var swal_text = data["swal_text"];
          } else {
            var swal_text = "Successfully Submited";
          }

          if (data["swal_button"]) {
            var swal_button = data["swal_button"];
          } else {
            var swal_button = "OK";
          }

          swal({
            title: swal_title,
            text: swal_text,
            icon: swal_icon,
            button: swal_button,
          }).then(function () {
            if (data["redirect_url"]) {
              location.href = data["redirect_url"];
            }
            if (data["reLoad"]) {
              location.reload();
            }

            if (data["click_class"]) {
              $(data["click_class"]).click();
            }
          });
        } else {
          $this.find(".ajax-form-error").text(data["error_message"]);
          swal({
            title: "Try Again !",
            text: data["error_message"],
            icon: "warning",
            button: "OK",
          });
        }
      },
      error: function (data) {
        swal({
          title: "Try Again !",
          text: "something went wrong",
          icon: "warning",
          button: "OK",
        });
      },
    });
  });

  $(".check_username").keyup(function (event) {
    let $this = $(this);
    var url = $this.attr("data-url");
    var method = "GET";
    let csrftoken = $("input[name='csrfmiddlewaretoken']").val();
    let value = $this.val();
    if (value.length > 5) {
      let data = "q=" + value + "&csrfmiddlewaretoken=" + csrftoken;

      $.ajax({
        type: method,
        url: url,
        dataType: "json",
        contentType: false,
        processData: false,
        data: data,

        success: function (data) {
          if (data["status"] == "true") {
            $(".check_username_msg").hide();
            $(".check_username_msg.valid-feedback").show();
          } else {
            $(".check_username_msg").hide();
            $(".check_username_msg.invalid-feedback").show();
          }
        },
        error: function (data) {
          swal({
            title: "Try Again !",
            text: "something went wrong",
            icon: "warning",
            button: "OK",
          });
        },
      });
    } else {
      $(".check_username_msg").hide();
      $(".check_username_msg.invalid-feedback").show();
    }
  });

  $(".search_and_view select").change(function () {
    let $this = $(this);
    let path = $this.parent(".search_and_view").attr("data-path") + $this.val();
    window.location = path;
  });
});
