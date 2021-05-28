function toggleVisibilityByClass(className)
{
	var elements = document.getElementsByTagName('div');
	for(var i = 0; i < elements.length; i++)
	{
		var node = elements.item(i);
        console.log(node.attributes);
		for(var j = 0; j < node.attributes.length; j++) 
		{
			if(node.attributes.item(j).nodeName == 'class') 
			{
				if(node.attributes.item(j).nodeValue.indexOf(className + ' ') == 0)
					node.style.display = ((node.style.display == "none") ? "block" : "none");
			}
		}
	}
}

function toggleVis(classname){
    // var elements = document.getElementsByTagName('div');
    var elements = document.getElementsByClassName(classname);
    console.log(elements);
    
}