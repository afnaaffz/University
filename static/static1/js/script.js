function addData(){
	var course=document.getElementById('course').value;
	var university=document.getElementById('university').value;
	var year=document.getElementById('year').value;

	if(course =="" || university =="" || year==""){
		alert("Please enter something first!");
	}else{
		var html="";

		html="<tr><td>"+course+"</td><td>"+university+"</td><td>"+year+"</td></tr>";

		document.getElementById('result').innerHTML+=html;

		document.getElementById('course').value="";
		document.getElementById('university').value="";
		document.getElementById('year').value="";
	}

}

function deleteRow(row) {
  var index = row.parentNode.parentNode.rowIndex;
  document.getElementById("row").deleteRow(index);
}