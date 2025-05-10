Introduction
Go does not have a concept of empty, null, or undefined for variable values. Variables declared without an explicit initial value default to the zero value for their respective type.

The zero value for primitive types such as booleans, numeric types, and strings are false, 0, and "", respectively.

The identifier nil, meaning zero, is the zero value for more complex types such as pointers, functions, interfaces, slices, channels, and maps.

The following table details the zero value for Go's types.

Type	Zero Value
boolean	false
numeric	0
string	""
pointer	nil
function	nil
interface	nil
slice	nil
channel	nil
map	nil
You may have noticed struct types are absent from the above table. That is because the zero value for a struct type depends on its fields. Structs are set to their zero value when all of its fields are set to their respective zero value.

Instructions
It is your job to prepare the city's IT system for an upcoming census. Specifically, you are responsible for the program that will process the data from the census workers.

The program must be able to create a new resident in the system when given a resident's information. Additionally, you will create functions that ensure the required information is present in the resident's data and delete a resident's data. Lastly, you will count the residents to provide an accurate census count.

When a census worker collects a resident's information, they need to register that resident by entering their name, age, and address into the system.

Implement the function NewResident that accepts three arguments:

The name of the resident.
The age of the resident.
The address of the resident.
The function should return a pointer to a Resident struct that holds this information.

name := "Matthew Sanabria"
age := 29
address := map[string]string{"street": "Main St."}

NewResident(name, age, address)
// => &{Matthew Sanabria 29 map[street:Main St.]}

Stuck? Reveal Hints
Opens in a modal
Residents may be reluctant to provide personal data to census workers. In those cases it's necessary to determine if the resident provided the required information to be counted in the census.

In order to be counted, a resident must provide a non-zero value for their name and an address that contains a non-zero value for the street key. All other information, such as the resident's age, is optional. Implement the HasRequiredInfo method that returns a boolean indicating if the resident has provided the required information.

name := "Matthew Sanabria"
age := 0
address := make(map[string]string)

resident := NewResident(name, age, address)

resident.HasRequiredInfo()
// => false

Stuck? Reveal Hints
Opens in a modal
Life moves fast and mistakes happen. A resident can move out of the city. A census worker can make mistakes when collecting data. In those cases, it's necessary to have the ability to delete a resident's data so they will not be counted.

Implement the Delete method that sets all of the fields the resident to their zero value.

name := "Matthew Sanabria"
age := 29
address := map[string]string{"street": "Main St."}

resident := NewResident(name, age, address)

fmt.Println(resident)
// Output: &{Matthew Sanabria 29 map[street:Main St.]}

resident.Delete()

fmt.Println(resident)
// Output: &{ 0 map[]}

Stuck? Reveal Hints
Opens in a modal
How to debug
When a test fails, a message is displayed describing what went wrong and for which input. You can also use the fact that console output will be shown too. You can write to the console using: