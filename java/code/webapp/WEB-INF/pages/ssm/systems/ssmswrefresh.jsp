<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean" %>
<%@ taglib uri="http://rhn.redhat.com/tags/list" prefix="rl" %>

<html:xhtml/>
<html>
  <body>
    <%@ include file="/WEB-INF/pages/common/fragments/ssm/header.jspf" %>
    <h2>
      <bean:message key="ssm.sw.systems.header" />
    </h2>
    <c:choose>
      <c:when test="${system_count > 0}">
        <c:choose>
          <c:when test="${system_count == 1}">
            <p><bean:message key="ssm.sw.systems.summary" arg0="${system_count} system"/></p>
          </c:when>
          <c:otherwise>
            <p><bean:message key="ssm.sw.systems.summary" arg0="${system_count} systems"/></p>
          </c:otherwise>
        </c:choose>
      </c:when>
      <c:otherwise>
        <p><bean:message key="ssm.sw.systems.summary.empty" /></p>
      </c:otherwise>
    </c:choose>

    <html:form action="/systems/ssm/misc/SoftwareRefresh.do">
      <html:hidden property="submitted" value="true"/>
        <div align="right">
          <html:submit>
            <bean:message key="ssm.sw.systems.confirmbutton"/>
          </html:submit>
        </div>
    </html:form>

  </body>
</html>
