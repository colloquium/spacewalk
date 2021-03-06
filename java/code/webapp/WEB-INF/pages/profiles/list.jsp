<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn" %>
<%@ taglib uri="http://rhn.redhat.com/tags/list" prefix="rl" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html" %>

<html:xhtml/>
<html>
<body>
<rhn:toolbar base="h1"
    img="/img/rhn-icon-packages.gif"
	imgAlt="profile.list.header.alt">
	<bean:message key="profile.list.header" />
</rhn:toolbar>
<div class="page-summary">
    <p><bean:message key="profile.list.summary"/></p>
</div>

<rl:listset name="groupSet">

    <rl:list dataset="pageList"
             width="100%"
             name="groupList"
             styleclass="list"
             emptykey="profile.list.noprofiles">

        <rl:column headerkey="column.name" bound="false">
            <a href="/rhn/profiles/Details.do?prid=${current.id}">
		        ${current.name}</a>
        </rl:column>

        <rl:column headerkey="column.basechannel">
              ${current.channelName}
        </rl:column>

        <rl:column headerkey="column.created">
              ${current.created}
        </rl:column>

    </rl:list>

</rl:listset>

</body>
</html>
