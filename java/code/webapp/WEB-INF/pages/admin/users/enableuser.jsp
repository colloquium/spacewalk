<%@ taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean" %>

<html:xhtml/>
<html>
<head>
    <meta name="name" value="User Details" />
</head>
<body>

<%@ include file="/WEB-INF/pages/common/fragments/user/user-header.jspf" %>

<h2><bean:message key="enableuser.jsp.confirm"/></h2>

<div class="page-summary">
    <bean:message key="enableuser.jsp.body"/>
</div>

<form method="POST" action="/rhn/users/EnableUserSubmit.do?uid=${param.uid}">
<div align="right">
      <hr />
      <html:submit>
          <bean:message key="enableuser.jsp.enable"/>
      </html:submit>
    </div>
</form>

</body>
</html>