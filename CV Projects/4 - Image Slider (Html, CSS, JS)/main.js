var slider_img = document.querySelector(".slider-img");
var images = [
  "Great-Wall-of-China.jpg",
  "Chichén Itzá.jpg",
  "Petra.jpg",
  "Machu Picchu.jpg",
  "Christ the Redeemer.jpg",
  "Colosseum.jpg",
  "Taj Mahal.jpg",
];

var i = 0;

const description = ["Great might be an understatement. One of the worlds largest building-construction projects, the Great Wall of China is widely thought to be about 5,500 miles (8,850 km) long; a disputed Chinese study, however, claims the length is 13,170 miles (21,200 km).", "Chichén Itzá is a Mayan city on the Yucatán Peninsula in Mexico, which flourished in the 9th and 10th centuries CE. Under the Mayan tribe Itzá—who were strongly influenced by the Toltecs—a number of important monuments and temples were built.", "The ancient city of Petra, Jordan, is located in a remote valley, nestled among sandstone mountains and cliffs. It was purported to be one of the places where Moses struck a rock and water gushed forth. Later the Nabataeans, an Arab tribe, made it their capital, and during this time it flourished, becoming an important trade center, especially for spices.", "This Incan site near Cuzco, Peru, was discovered in 1911 by Hiram Bingham, who believed it was Vilcabamba, a secret Incan stronghold used during the 16th-century rebellion against Spanish rule. Although that claim was later disproved, the purpose of Machu Picchu has confounded scholars. ", "Christ the Redeemer, a colossal statue of Jesus, stands atop Mount Corcovado in Rio de Janeiro. Its origins date to just after World War I, when some Brazilians feared a tide of godlessness.", "The Colosseum in Rome was built in the first century by order of the Emperor Vespasian. A feat of engineering, the amphitheater measures 620 by 513 feet (189 by 156 meters) and features a complex system of vaults.", "This mausoleum complex in Agra, India, is regarded as one of the worlds most iconic monuments and is perhaps the finest example of Mughal architecture. It was built by Emperor Shah Jahān (reigned 1628 to 58) to honor his wife Mumtāz Maḥal, who died in 1631 giving birth to their 14th child."];

	window.onload = init;

	function init()
	{
		paragraph.textContent = description[i];
	}

var paragraph = document.getElementById("p");

	function prev()
	{
    		// console.log(i);
    
	if (i <= 0)
	{
		i = images.length-1;
		paragraph.textContent = description[i];
	}
	else if(i>images.length-1)
	{
    		i--; 
		paragraph.textContent = description[i];
	}
  	else
	{ 
  		i--;
		paragraph.textContent = description[i];
  	}
  
	return setImg();
	}

	function next() 
	{
    		// console.log(i);
    
	if(i>=images.length-1)
	{
		i=0;
		paragraph.textContent = description[i];
	}
	else if(i<images.length-1)
	{
    		i++; 
		paragraph.textContent = description[i];
	}

	return setImg();
	}

	function setImg()
	{
    		// console.log(i);
  		return slider_img.setAttribute("src", "images/" + images[i]);
	}