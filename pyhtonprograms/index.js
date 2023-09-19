data = "All string methods returns new values. They do not change the original string.";
const person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  fullName: function () {
    return this.firstName + " " + this.lastName;
  },
};
person.fullName()
person.firstName.lastIndexOf()
