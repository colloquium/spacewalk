<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean" %>
<%@ taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html" %>

<html:html xhtml="true">
    <body>
        <%@ include file="/WEB-INF/pages/common/fragments/systems/system-header.jspf" %>
        <h2>
            <img src="/img/rhn-icon-channels.gif" alt="channel"/>
            <bean:message key="sdc.channels.confirmNewBase.header.confirm"/>
        </h2>

        <bean:message key="sdc.channels.confirmNewBase.currentlySubscribedTo"/><p/>
        <c:choose>
            <c:when test="${current_base_channel == null}">
                <strong><bean:message key="sdc.channels.confirmNewBase.noBaseChannel"/></strong>
            </c:when>
            <c:otherwise>
                <ul class="channel-list">
                    <li><a href="/rhn/channels/ChannelDetail.do?cid=${current_base_channel.id}">${current_base_channel.name}</a></li>
                    <c:forEach items="${current_preserved_child_channels}" var="current">
                        <li class="child-channel">${current.name}</li>
                    </c:forEach>
                    <c:forEach items="${current_unpreserved_child_channels}" var="current">
                        <li class="child-channel highlighted">${current.name}</li>
                    </c:forEach>
                </ul>
            </c:otherwise>
        </c:choose>
        <p/>

        <bean:message key="sdc.channels.confirmNewBase.toBeSubscribedTo"/><p/>
        <c:choose>
            <c:when test="${new_base_channel == null}">
                <strong><bean:message key="sdc.channels.confirmNewBase.noBaseChannel"/></strong>
            </c:when>
            <c:otherwise>
                <ul class="channel-list">
                    <li><a href="/rhn/channels/ChannelDetail.do?cid=${new_base_channel.id}">${new_base_channel.name}</a></li>
                    <c:forEach items="${preserved_child_channels}" var="current">
                        <li class="child-channel">${current.name}</li>
                    </c:forEach>
                </ul>
            </c:otherwise>
        </c:choose>
        <p/>

        <bean:message key="sdc.channels.confirmNewBase.otherChannelsWarning"/>
        <p/>&nbsp;<p/>

        <span class="small-text">
            <bean:message key="sdc.channels.confirmNewBase.fasTrackBetaNote"/>
        </span>

        <html:form method="post" action="/systems/details/SystemChannels.do?sid=${system.id}">
            <div align="right">
                <html:hidden property="submitted" value="true"/>
                <html:hidden property="new_base_channel_id" value="${new_base_channel_id}"/>
                <html:submit property="dispatch">
                    <bean:message key="sdc.channels.confirmNewBase.cancel"/>
                </html:submit>

                <html:submit property="dispatch">
                    <bean:message key="sdc.channels.confirmNewBase.modifyBaseSoftwareChannel"/>
                </html:submit>
            </div>
        </html:form>

    </body>
</html:html>

