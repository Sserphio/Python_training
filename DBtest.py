{
  "id": "f720f9a3-c9e0-448f-919d-a187ab0f7e8d",
  "version": "2.0",
  "name": "DBtest",
  "url": "http://localhost",
  "tests": [{
    "id": "d0147e22-299a-4876-838c-ab07150aa1f5",
    "name": "DBtest",
    "commands": [{
      "id": "5e6a52b0-16ca-4230-9bc4-5566aed8c369",
      "comment": "",
      "command": "open",
      "target": "/phpmyadmin/index.php",
      "targets": [],
      "value": ""
    }, {
      "id": "1cd94fe4-7069-46f8-a134-b3d23c101ce2",
      "comment": "",
      "command": "setWindowSize",
      "target": "1936x1176",
      "targets": [],
      "value": ""
    }, {
      "id": "8de53403-73b9-4b85-9bc9-74956a5a5b69",
      "comment": "",
      "command": "click",
      "target": "linkText=New",
      "targets": [
        ["linkText=New", "linkText"],
        ["css=.first > .hover_show_full", "css:finder"],
        ["xpath=//a[contains(text(),'New')]", "xpath:link"],
        ["xpath=//div[@id='pma_navigation_tree_content']/ul/li/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'index.php?route=/server/databases')])[2]", "xpath:href"],
        ["xpath=//div[2]/div[3]/ul/li/a", "xpath:position"],
        ["xpath=//a[contains(.,'New')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "91f5978f-2a79-4280-a164-56d872255aa1",
      "comment": "",
      "command": "click",
      "target": "name=db_collation",
      "targets": [
        ["name=db_collation", "name"],
        ["css=.form-select", "css:finder"],
        ["xpath=//select[@name='db_collation']", "xpath:attributes"],
        ["xpath=//form[@id='create_database_form']/div[2]/select", "xpath:idRelative"],
        ["xpath=//div[2]/select", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "5f6ee9c6-bf33-429d-adde-0b7042215c27",
      "comment": "",
      "command": "select",
      "target": "name=db_collation",
      "targets": [],
      "value": "label=utf8mb4_general_ci"
    }, {
      "id": "4efd82e5-8941-4269-a713-d72d3c442d24",
      "comment": "",
      "command": "click",
      "target": "id=text_create_db",
      "targets": [
        ["id=text_create_db", "id"],
        ["name=new_db", "name"],
        ["css=#text_create_db", "css:finder"],
        ["xpath=//input[@id='text_create_db']", "xpath:attributes"],
        ["xpath=//form[@id='create_database_form']/div/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "98257ba6-bb75-4713-bbe0-4af64a4b65ee",
      "comment": "",
      "command": "type",
      "target": "id=text_create_db",
      "targets": [
        ["id=text_create_db", "id"],
        ["name=new_db", "name"],
        ["css=#text_create_db", "css:finder"],
        ["xpath=//input[@id='text_create_db']", "xpath:attributes"],
        ["xpath=//form[@id='create_database_form']/div/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": "addressbook"
    }, {
      "id": "d7fe7cf6-efdf-48da-bb98-f12a9f86e346",
      "comment": "",
      "command": "click",
      "target": "id=buttonGo",
      "targets": [
        ["id=buttonGo", "id"],
        ["css=#buttonGo", "css:finder"],
        ["xpath=//input[@id='buttonGo']", "xpath:attributes"],
        ["xpath=//form[@id='create_database_form']/div[3]/input", "xpath:idRelative"],
        ["xpath=//div[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "af0fc09a-f345-4e4d-abb9-efb31fb04577",
      "comment": "",
      "command": "mouseOver",
      "target": "id=buttonGo",
      "targets": [
        ["id=buttonGo", "id"],
        ["css=#buttonGo", "css:finder"],
        ["xpath=//input[@id='buttonGo']", "xpath:attributes"],
        ["xpath=//form[@id='create_database_form']/div[3]/input", "xpath:idRelative"],
        ["xpath=//div[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b7150ce7-e21f-4928-973a-12fbc4a5a422",
      "comment": "",
      "command": "click",
      "target": "css=.ic_b_import",
      "targets": [
        ["css=.ic_b_import", "css:finder"],
        ["xpath=//img[@alt='Import']", "xpath:img"],
        ["xpath=//ul[@id='topmenu']/li[6]/a/img", "xpath:idRelative"],
        ["xpath=//li[6]/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ac5fbb9b-731f-4c9d-8819-6e605ff70737",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.ic_b_import",
      "targets": [
        ["css=.ic_b_import", "css:finder"],
        ["xpath=//img[@alt='Import']", "xpath:img"],
        ["xpath=//ul[@id='topmenu']/li[6]/a/img", "xpath:idRelative"],
        ["xpath=//li[6]/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "da5f15a8-e3fc-4d6e-a29d-a4933865c67a",
      "comment": "",
      "command": "click",
      "target": "id=input_import_file",
      "targets": [
        ["id=input_import_file", "id"],
        ["name=import_file", "name"],
        ["css=#input_import_file", "css:finder"],
        ["xpath=//input[@id='input_import_file']", "xpath:attributes"],
        ["xpath=//form[@id='import_file_form']/div/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "20fb84e6-c314-481f-abf4-7ce588d11950",
      "comment": "",
      "command": "type",
      "target": "id=input_import_file",
      "targets": [
        ["id=input_import_file", "id"],
        ["name=import_file", "name"],
        ["css=#input_import_file", "css:finder"],
        ["xpath=//input[@id='input_import_file']", "xpath:attributes"],
        ["xpath=//form[@id='import_file_form']/div/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": "C:\\fakepath\\addressbook111.sql"
    }, {
      "id": "bbb2e4e8-a98a-4b5b-b45d-4cf07f48b4c8",
      "comment": "",
      "command": "click",
      "target": "id=buttonGo",
      "targets": [
        ["id=buttonGo", "id"],
        ["css=#buttonGo", "css:finder"],
        ["xpath=//input[@id='buttonGo']", "xpath:attributes"],
        ["xpath=//div[@id='submit']/input", "xpath:idRelative"],
        ["xpath=//div[6]/input", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "bb868909-af18-4291-8c8d-d863f9d122b9",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["d0147e22-299a-4876-838c-ab07150aa1f5"]
  }],
  "urls": ["http://localhost/"],
  "plugins": []
}