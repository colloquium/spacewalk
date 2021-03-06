<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean" %>

<html:xhtml/>
<html>

<body>
<%@ include file="/WEB-INF/pages/common/fragments/systems/system-header.jspf" %>

<rhn:require acl="is_solaris()">
	<h2>
		<img src="/img/rhn-icon-package_add.gif" />
		<bean:message key="packagelist.jsp.confirmpatchinstall" />
	</h2>
	<div class="page-summary">
		<p>
		${requestScope.pageSummary}
		</p>
	</div>
</rhn:require>

<form method="POST" name="rhn_list" action="/rhn/systems/details/packages/patches/PatchInstallConfirmSubmit.do">
<rhn:list pageList="${requestScope.pageList}" noDataText="packagelist.jsp.nopatches" >
  <rhn:listdisplay filterBy="packagelist.jsp.packagename" >
    <rhn:column header="packagelist.jsp.patchname"
                url="/rhn/software/packages/Details.do?sid=${param.sid}&id_combo=${current.idCombo}">
      ${current.nvre}
    </rhn:column>
    <rhn:column header="packagelist.jsp.patchtype">
      ${current.patchType}
    </rhn:column>
  </rhn:listdisplay>
  <div align="right">
      <hr />
      <html:submit property="dispatch">
      <bean:message key="packagelist.jsp.confirmpatchinstall"/>
      </html:submit>
  </div>
</rhn:list>
<input type="hidden" name="sid" value="${param.sid}" />
</form>
</body>
</html>
