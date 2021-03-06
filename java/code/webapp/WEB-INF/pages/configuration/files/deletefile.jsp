<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn"%>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean"	prefix="bean"%>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-html"	prefix="html"%>

<html:xhtml/>
<html>
<head></head>
<body>
<%@ include file="/WEB-INF/pages/common/fragments/configuration/files/manage_header.jspf"%>

<h2><bean:message key="deletefile.jsp.header2" /></h2>
<bean:message key="deletefile.jsp.info" />
<p />
<html:form action="/configuration/file/DeleteFile.do?cfid=${cfid}">
	<html:hidden property="submitted" value="true"/>
	<table class="details">
	<tr>
		<th><bean:message key="deleterev.jsp.channelname" /></th>
		<td>${file.configChannel.displayName}</td>
	</tr>
	<tr>
		<th><bean:message key="deleterev.jsp.revisionpath" /></th>
		<td>${file.configFileName.path}</td>
	</tr>
	<c:if test="${!revision.directory}">
	  <tr>
		<th><bean:message key="deletefile.jsp.totalspace" /></th>
		<td>${storage}</td>
	  </tr>
	</c:if>
	</table>
	<hr />
	<div align="right">
	  <html:submit><bean:message key="deletefile.jsp.submit" /></html:submit>
	</div>
</html:form>
	
</body>
</html>	