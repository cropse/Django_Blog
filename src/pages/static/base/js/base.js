$(document).ready(function(){
  $(".content-markdown").each(function(){
    var content = $(this).text()
    // console.log(content)
    var markedContent = marked(content)
    // console.log(markedContent)
    $(this).html(markedContent)
  })
  $(".post-detail-item img").each(function(){
    $(this).addClass("img-responsive")
  })

  var contentInput = $("#cke_1_contents iframe")

  console.log(contentInput).text()
  function setContent(value){
    // syn content function
    var markedContent = marked(value)
    $("#preview-content").html(markedContent)
    $("#preview-content img").each(function(){
      $(this).addClass("img-responsive")
    })
  }

  setContent(contentInput.val())// init

  contentInput.keyup(function(){
    // set keyup function
    console.log("123")
    setContent($(this).val())  
  })

  var titleInput = $("#id_title")
  $("#preview-title").text(titleInput.val())// init

  function setTitle(value){
    // syn title function
    $("#preview-title").text(value)
  }

  titleInput.keyup(function(){
    // set keyup function
    setTitle($(this).val())  
  })