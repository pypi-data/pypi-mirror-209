from .base import HTMLTemplate

class OpenApiTemplate(HTMLTemplate):
    """HTML Template class with OpenAPI format"""

    def getHead(self):
        return self.__HEAD

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
    
    def getPropertiesPartUpCategory(self):
        return self.__PROPERTIES_PART_UP_CATEGORY
    
    def getPropertiesPartDownCategory(self):
        return self.__PROPERTIES_PART_DOWN_CATEGORY

    __HEAD = """
  <head>
    <title>Activo</title>

    <link rel="icon" type="image/png" href="http://ostranme.github.io/swagger-ui-themes/demo/images/favicon-32x32.png" sizes="32x32">
    <link rel="icon" type="image/png" href="http://ostranme.github.io/swagger-ui-themes/demo/images/favicon-16x16.png" sizes="16x16">
    <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/typography.css" media="screen" rel="stylesheet" type="text/css">
    <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/reset.css" media="screen" rel="stylesheet" type="text/css">
    <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/screen.css" media="screen" rel="stylesheet" type="text/css">
    <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/reset.css" media="print" rel="stylesheet" type="text/css">
    <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/print.css" media="print" rel="stylesheet" type="text/css">

    <!-- Swagger UT theme -->
    <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/screen.css" media="screen" rel="stylesheet" id="sut" type="text/css">

    <style>

        .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations li.operation.none div.content {
        background-color: #ddd8d2;
        border: 1px solid #f0e0ca;
        }

        .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations li.operation.good div.content {
        background-color: #f6f9e3;
        border: 1px solid #f2f77f;
        }

        .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations li.operation div.heading h3 span.http_method a {
        text-transform: uppercase;
        color: white;
        display: inline-block;
        width: 70px;
        font-size: 0.7em;
        text-align: center;
        padding: 7px 10 4px;
        -moz-border-radius: 2px;
        -webkit-border-radius: 2px;
        -o-border-radius: 2px;
        -ms-border-radius: 2px;
        -khtml-border-radius: 2px;
        border-radius: 2px;
        }
        
        .swagger-section .swagger-ui-wrap {
            min-width: 760px;
            max-width: 1400px;
        }

        .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations.grupal {
            padding-bottom: 12px;
        }

        .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations.grupal > li div.heading {
            background-color: burlywood;
        }

        .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations.grupal > li div.heading h2 {
            color: white;
            padding-left: 12px;
        }

    </style>

  </head>
        """

    __BODY_HEAD = """
    <div id="header">
      <div class="swagger-ui-wrap">
        <a id="logo" href="http://swagger.io/">
          <img class="logo__img" alt="IsyHub-Aubay-Logo" height="30" src="https://lab.isyhub.net/assets/theme/isyhub/images/logos/default.png">
          <span class="logo__title">Activos</span>
        </a>
      </div>
    </div>
            """

    __INFO_CATEGORY = """
      <li class="resource active">
        <div class="heading">
          <h2>Información General</h2>
          <ul class="endpoints">
            <li class="endpoint">
              <ul class="operations">
                <li class="post operation">
                  <div class="heading">
                    <h3>
                      <span class="http_method">
                        <a href="" class="toggleOperation">Nombre</a>
                      </span>
                      <span class="path">
                        <a href="" class="toggleOperation ">${name}</a>
                      </span>
                    </h3>
                  </div>
                  <div class="content">
                    <div class="response-class">
                      <h4><span data-sw-translate="">Descripción</span></h4>
                      <div class="markdown">
                        <p>${description}</p>
                      </div>
                      <br>
                    </div>
                    <form accept-charset="UTF-8" class="sandbox">
                      <table class="fullwidth parameters">
                        <tbody class="operation-params">
                          ${row_list}
                        </tbody>
                      </table>
                    </form>
                  </div>
                </li>
              </ul>
            </li>

          </ul>
        </div>

      </li>
                """

    __ITEM_LIST = """
                          <tr>
                            <td class="code required"><label>${key}</label></td>
                            <td>
                              <strong><span class="markdown">
                                  <p>${value}</p>
                                </span></strong>
                            </td>
                            <td>${title}</td>
                          </tr>
            """

    __LABEL_PROPERTIES_CATEGORY = """
                            <th style="width: 100px; max-width: 100px" data-sw-translate="">${label}</th>
                            """
    
    __VALUE_PROPERTIES_CATEGORY = """
<td class="code"><label>${value}</label></td>
                            """
    
    __PROPERTIES_ITEM_CATEGORY = """
                <li class="${color} operation">
                  <div class="content">
                    <form accept-charset="UTF-8" class="sandbox">
                      <table class="fullwidth parameters">
                        <thead>
                          <tr>
                            ${labels}
                          </tr>
                        </thead>
                        <tbody class="operation-params">
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
