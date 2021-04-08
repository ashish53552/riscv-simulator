var tables = $("table");
(function () {
    tables.hide().first().show();
    //Hides all the tables except first
    $("a.button").on("click", function () {
        //Adds eventListner to buttons
        tables.hide();
        //Hides all the tables
        var tableTarget = $(this).data("table");
        //Gets data# of button
        $("table#" + tableTarget).show();
        //Shows the table with an id equal to data attr of the button
    })
})();


