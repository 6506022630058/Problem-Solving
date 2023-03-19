function ddlselect()
{
  var d = document.getElementById("ddselect");
  var displaytext=d.options[d.selectedIndex].text;

  document.getElementById("txtvalue1").innerHTML=displaytext+' eat';
  document.getElementById("txtvalue2").innerHTML=displaytext+' was eaten';
}