<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html" %>
<%@ taglib uri="http://rhn.redhat.com/tags/list" prefix="rl" %>

<html:html xhtml="true">
<body>

<%@ include file="/WEB-INF/pages/common/fragments/systems/system-header.jspf" %>

<div class="toolbar-h2">
  <img src="/img/rhn-icon-info.gif" alt="" />
  <bean:message key="system.jsp.customkey.updatetitle"/>
</div>

  <hr />

    <rl:listset name="keySet">

        <rl:list dataset="pageList"
            name="keyList"
            emptykey="system.jsp.customkey.empty"
            alphabarcolumn="label"
            filter="com.redhat.rhn.frontend.taglibs.list.filters.CustomKeyOverviewFilter">

          <rl:column sortable="true"
              bound="false"
              headerkey="system.jsp.customkey.keylabel"
              sortattr="label"
              defaultsort="asc"
              styleclass="first-column">

            <a href="/rhn/systems/details/UpdateCustomData.do?sid=${system.id}&cikid=${current.id}">
              <c:out value="${current.label}" />
            </a>
          </rl:column>

           <rl:column sortable="false"
               bound="false"
               headerkey="system.jsp.customkey.description"
              styleclass="last-column">
             <c:out value="${current.description}" />
          </rl:column>

        </rl:list>

    </rl:listset>
  </body>
</html:html>
