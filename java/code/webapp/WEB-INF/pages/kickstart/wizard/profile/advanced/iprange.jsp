<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html" %>

<html:html xhtml="true">
<body>
<%@ include file="/WEB-INF/pages/common/fragments/kickstart/advanced/header.jspf"%>
<c:import url="/WEB-INF/pages/common/fragments/kickstart/ipranges.jspf">
	<c:param name = "range_delete_url" value="/rhn/kickstart/KickstartIpRangeDeleteAdvanced.do"/>
	<c:param name = "range_edit_url" value="/kickstart/KickstartIpRangeEditAdvanced.do"/>	
</c:import>
</body>
</html:html>

