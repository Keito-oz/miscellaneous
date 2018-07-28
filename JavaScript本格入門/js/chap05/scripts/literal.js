var Member = function(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
};

Member.prototype.getName = function() {
  return this.lastName + ' ' + this.firstName;
};

Member.prototype.toString = function() {
  return this.lastName + this.firstName;
};

var mem = new Member('祥寛', '山田');
console.log(mem.getName());
console.log(mem.toString());
