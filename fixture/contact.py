from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.telephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("submit").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_new_contact_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_new_contact_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        wd.find_element_by_xpath("//tr[%d]/td[8]/a/img" % (int(index)+2)).click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.telephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % str(id)).click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.telephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_new_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_new_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=address,
                                                  all_phones=all_phones, all_emails=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_new_contact_page()
        wd.find_element_by_xpath("//tr[%d]/td[8]/a/img" % (int(index)+2)).click()
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        telephone = wd.find_element_by_name("home").get_attribute("value")
        telephone2 = wd.find_element_by_name("work").get_attribute("value")
        telephone3 = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(lastname=lastname, firstname=firstname, id=id, address=address, telephone=telephone,
                       telephone2=telephone2, telephone3=telephone3, email=email, email2=email2, email3=email3)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.open_new_contact_page()
        wd.find_element_by_css_selector("input[value='%s']" % str(contact.id)).click()
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("//option[2]") # как выбрать необходимую группу если имена не уникальны?
        wd.find_element_by_css_selector("input[value='Add to']").click()
