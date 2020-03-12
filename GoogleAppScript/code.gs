function AllTestBankForms() {
  var dataFolder = DriveApp.getFoldersByName("JSON_EconTestBanks").next();
  var classFolders = dataFolder.getFolders();    //APMicro, APMacro
  
  while (classFolders.hasNext()) {
    var classFolder = classFolders.next();
    var currentClass = classFolder.getName();
    var unitFolders = classFolder.getFolders();
    
    while (unitFolders.hasNext()) {
      var unitFolder = unitFolders.next();
      var currentUnit = unitFolder.getName();
      var files = unitFolder.getFiles();
      
      while (files.hasNext()) {
          var file = files.next();
          JSON2Form(file, currentClass, currentUnit);
      }
    }
  } 
}

/*
function tester() {
  var files = DriveApp.getFilesByName('u1-1.json')
  var file = files.next();
  var currentClass = 'APMicro';
  var currentUnit = 'APU1';
  JSON2Form(file, currentClass, currentUnit);
}
*/

function JSON2Form(file, currentClass, currentUnit) {
  var jsonFile = file.getAs('application/json');
  var jsonName = file.getName();
  var jsonObj = JSON.parse(jsonFile.getDataAsString());
  
  // TODO: Format Title String for each test bank
  var titleString = currentClass.slice(2).concat(' Unit ', currentUnit.charAt(3), ': Test Bank ', jsonName.charAt(3)); 
  var form = FormApp.create(titleString);
  form.setIsQuiz(true);
  var problem;
  var item;
  var questionStatement;
  var images;
  var answerChoices;
  var itemChoices;
  var answer;
  var answerN;
  
  for (let i = 0; i < jsonObj.length; i++) {
    problem = jsonObj[i]
    questionStatement = problem.QuestionStatement
    images = problem.Images
    answerChoices = problem.AnswerChoices
    answer = problem.Answer
    // "A" -> 0, "B" -> 1, "C" -> 2, etc.
    answerN = answer.toUpperCase().charCodeAt(0) - 65
    
    item = form.addMultipleChoiceItem();
    item.setTitle(questionStatement);
    item.setChoices(answerChoices.map(function(choice, i) {
      return item.createChoice(choice, i==answerN);
    }));
    if (images.length > 0) {
      item.setHelpText(images.join(', \n'));
    }
  }
  // TODO: move form to folder
  var formID = form.getId();
  var saveFolder = DriveApp.getFoldersByName('EconTestBankForms').next();
  saveFolder.addFile(DriveApp.getFileById(formID));
}