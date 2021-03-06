<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn" %>
<%@ taglib uri="http://rhn.redhat.com/tags/config-managment" prefix="cfg" %>
<%@ taglib uri="http://rhn.redhat.com/tags/list" prefix="rl" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html" %>

<html:xhtml/>
<html>
<body>

<%@ include file="/WEB-INF/pages/common/fragments/ssm/header.jspf" %>
<h2>
  <img src="/img/rhn-config_channels.gif" alt='<bean:message key="config.common.channelsAlt" />' />
  <bean:message key="ssm.config.subscribeconfirm.jsp.header"/>
</h2>
<h3><bean:message key="ssm.config.subscribeconfirm.jsp.step"/></h3>
<div class="page-summary">
  <p>
    <bean:message key="ssm.config.subscribeconfirm.jsp.summary"/> <br />
    <c:choose>
      <c:when test="${param.position eq 'replace'}">
        <bean:message key="ssm.config.subscribeconfirm.jsp.replacesummary" />
      </c:when>
      <c:when test="${param.position eq 'lowest'}">
        <bean:message key="ssm.config.subscribeconfirm.jsp.lowestsummary" />
      </c:when>
      <c:when test="${param.position eq 'highest'}">
        <bean:message key="ssm.config.subscribeconfirm.jsp.highestsummary" />
      </c:when>
    </c:choose>
  </p>
</div>

<rl:listset name="confirmListSet">
<!-- Start of system list -->
<rl:list dataset="systemList"
         width="100%"
         name="systemList"
         styleclass="list"
         emptykey="ssm.config.subscribeconfirm.jsp.noSystems">
  <!-- column system name -->
  <rl:column bound="false"
             sortable="true"
             headerkey="system.common.systemName"
             styleclass="first-column"
             attr="name">
    <a href="/rhn/systems/details/configuration/Overview.do?sid=${current.id}">
      <img src="/img/rhn-listicon-system.gif"
             alt="<bean:message key='system.common.systemAlt' />" />
      ${current.name}
    </a>
  </rl:column>
  <!-- column config channel count -->
  <rl:column bound="false"
             sortable="false"
             headerkey="ssm.config.subscribeconfirm.jsp.currentchannels"
             styleclass="last-column"
             attr="configChannelCount">
    <c:choose>
      <c:when test="${current.configChannelCount eq 1}">
        <bean:message key="ssm.config.subscribeconfirm.jsp.onesubscription" />
      </c:when>
      <c:otherwise>
        <bean:message key="ssm.config.subscribeconfirm.jsp.numsubscriptions"
                      arg0="${current.configChannelCount}" />
      </c:otherwise>
    </c:choose>
  </rl:column>
</rl:list>

<!-- Start of channel list -->
<rl:list dataset="channelList"
         width="100%"
         name="channelList"
         styleclass="list"
         emptykey="ssm.config.subscribeconfirm.jsp.noChannels">
  <!-- column config channel name -->
  <%-- This column is not sortable solely because the order that the
       config channels appear is the order that they will be subscribed in --%>
  <rl:column bound="false"
             sortable="false"
             headerkey="config.common.configChannel"
             styleclass="first-column"
             attr="name">
    <cfg:channel id="${current.id}" name="${current.name}" type="central" />
  </rl:column>
  <!-- column files and dirs count -->
  <rl:column bound="true"
             sortable="false"
             headerkey="ssm.config.subscribeconfirm.jsp.files"
             attr="filesAndDirsDisplayString" />
  <!-- column system count -->
  <rl:column bound="false"
             sortable="false"
             headerkey="ssm.config.subscribeconfirm.jsp.currentsystems"
             attr="systemCount">
    <c:choose>
      <c:when test="${current.systemCount eq 1}">
        <bean:message key="ssm.config.subscribeconfirm.jsp.onesubscription" />
      </c:when>
      <c:otherwise>
        <bean:message key="ssm.config.subscribeconfirm.jsp.numsubscriptions"
                      arg0="${current.systemCount}" />
      </c:otherwise>
    </c:choose>
  </rl:column>
</rl:list>
</rl:listset>

<html:form method="POST" action="/systems/ssm/config/SubscribeConfirm.do?position=${param.position}">
    <div align="right">
      <hr />
      <html:submit property="dispatch">
        <bean:message key="ssm.config.subscribeconfirm.jsp.confirm" />
      </html:submit>
    </div>
</html:form>
</body>
</html>
