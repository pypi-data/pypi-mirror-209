class HTMLTemplate:
    """HTML Template class"""

    def __init__(self):
        self.data = []
    
    def getHead(self):
        return """
  <head>
    <title>Activo</title>
    <style>
    </style>
  </head>
        """

    def getBodyHead(self):
        return self.__BODY_HEAD

    def getItemList(self):
        return self.__ITEM_LIST

    def getInfoCategory(self):
        return self.__INFO_CATEGORY
    
    def getLabelPropertiesCategory(self):
        return self.__LABEL_PROPERTIES_CATEGORY

    def getValuePropertiesCategory(self):
        return self.__VALUE_PROPERTIES_CATEGORY
    
    def getPropertiesItemCategory(self):
        return self.__PROPERTIES_ITEM_CATEGORY
    
    def getPropertiesCategory(self):
        return self.__PROPERTIES_CATEGORY

    __BODY_HEAD = """
    <div id="header">
        Activos
    </div>
            """

    __INFO_CATEGORY = """
      <li>
        <div>
          <h2>Información General</h2>
          <ul>
            <li>
                <div>
                    <span>
                    <a href="">Nombre</a>
                    </span>
                    <span class="path">
                    <a href="">${name}</a>
                    </span>
                </div>
                <div>
                <div>
                    <h4><span>Descripción</span></h4>
                    <div>
                    <p>${description}</p>
                    </div>
                    <br>
                </div>
                <form accept-charset="UTF-8">
                    <table>
                    <tbody>
                        ${row_list}
                    </tbody>
                    </table>
                </form>
                </div>
            </li>
          </ul>
        </div>

      </li>
                """

    __ITEM_LIST = """
                          <tr>
                            <td><label>${key}</label></td>
                            <td>
                              <strong><span>
                                  <p>${value}</p>
                                </span></strong>
                            </td>
                            <td>${title}</td>
                          </tr>
            """

    __LABEL_PROPERTIES_CATEGORY = """
                            <th>${label}</th>
                            """
    
    __VALUE_PROPERTIES_CATEGORY = """
<td class="code"><label>${value}</label></td>
                            """
    
    __PROPERTIES_ITEM_CATEGORY = """
                <li class="${color}">
                  <div>
                    <form accept-charset="UTF-8">
                      <table>
                        <thead>
                          <tr>
                            ${labels}
                          </tr>
                        </thead>
                        <tbody>
                          ${row_list}
                        </tbody>
                      </table>
                    </form>
                  </div>
                </li>
                    """
    
    __PROPERTIES_PART_UP_CATEGORY = """
      <li class="resource">
        <div class="heading">
          <h2>${title}</h2>
          <ul class="endpoints">
            <li class="endpoint">
              <ul class="operations">
                    """
    
    __PROPERTIES_PART_DOWN_CATEGORY = """
              </ul>
            </li>

          </ul>
        </div>
      </li>
                    """
    
    __PROPERTIES_CATEGORY = __PROPERTIES_PART_UP_CATEGORY + """
                ${item_list}
                                                    """ + __PROPERTIES_PART_DOWN_CATEGORY
