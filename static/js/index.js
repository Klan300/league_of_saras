document.getElementById("btn").onclick = function() {btn()};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function btn() {
    $(".describe").addClass("fadeout");
    await sleep(500);
    $(".description").addClass("hide");
    $(".start").addClass("hide");
    $(".form").addClass("views");
    $(".home").addClass("smaller");
}
