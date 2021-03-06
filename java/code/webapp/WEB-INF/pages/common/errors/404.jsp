<%@ taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean" %>
<%@ taglib uri="http://www.opensymphony.com/sitemesh/page" prefix="page" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>
<%@ page contentType="text/html; charset=UTF-8" %>
<html:xhtml/>
<page:applyDecorator name="layout_c">
<body>
    <c:set value="${requestScope[&quot;javax.servlet.error.request_uri&quot;]}" var="errorUrl" />
    <c:set var="escapedUrl" value="${fn:escapeXml(errorUrl)}"/>

    <h1>
      <img src="/img/rhn-icon-warning.gif"
           alt="<bean:message key='500.jsp.imgAlt' />" />
      <bean:message key="404.jsp.title"/>
    </h1>
    <p><bean:message key="404.jsp.summary" arg0="${escapedUrl}"/></p>
    <ol>

      <li><bean:message key="404.jsp.reason1"/></li>
      <li><bean:message key="404.jsp.reason2" arg0="${escapedUrl}"/></li>
      <li><bean:message key="404.jsp.reason3" arg0="${escapedUrl}"/></li>
      <li><bean:message key="404.jsp.reason4"/></li>
    </ol>
</body>
</page:applyDecorator>
