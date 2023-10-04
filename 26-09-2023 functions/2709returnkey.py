#here we are calling one function to chekc weter the number is prime or not by uing the loop concept

mylist=[7,10,19,78,56,59]


def oddnumber(number):
    if number%2!=0:
        return number
    else:
        print("number is evenr")
#oddnumber(21)
        

#local vs global
number=30
print(number)
def local():
    global number #here we call
    number=10  # where ever the name varible is present in tat place it is updated (ut again code will not run from top to bottom)
    print(number+10)
local()  
print(number)

#local vs global

def local(): here number variable have life upto local once the function executed then it will go for dead mode dude to that only if we call the varible out side it is not wotking
    number=10
    print(number+10)
local()  
print(number)


#local vs global
number=30
def local():
    number=10
    print(number+10)
local()  
print(number)


#local vs global
number=30
print(number)
def local():
    global number #here we call
    number=10  # where ever the name varible is present in tat place it is updated (ut again code will not run from top to bottom)
    print(number+10)
local()  
print(number)

let allCit1 = $(editor.getBody()).find('.REFLINK');

allCit1.each((index, citele) => {
  $(citele).on('mouseenter', (e) => {
    let targetHash = e.currentTarget.hash;
    debugger
    let refele = tinymce.activeEditor.getBody().querySelector(targetHash);
     let refele1 = document.querySelector('.popup-style')
    if (!refele1) {
      debugger
    if (refele) {
      // Create a popup element
      let popup = document.createElement('div');
      popup.classList.add('popup-style'); // Apply your CSS class for styling

      // Set the text content of the popup
      popup.textContent = refele.textContent;

      // Apply background color
      popup.style.background = '#eaeaea'; // Replace with your desired background color

      // Append the popup to the body
      document.body.appendChild(popup);

      // Position the popup based on mouse position
      popup.style.position = 'absolute';
      popup.style.top = e.clientY + 'px';
      popup.style.left = e.clientX + 'px';

      
    }
    }
    $(citele).on('mouseleave', () => {
      debugger
          popupDisplayed = false; // Reset the flag
          $('.popup-style').remove();
        });
  });
});


