/*
	A simple, lightweight jQuery plugin for creating sortable tables.
	https://github.com/kylefox/jquery-tablesort
	Version 0.0.11
*/
!function(t) {
    t.tablesort = function(e, s) {
        var i = this;
        this.$table = e,
        this.$thead = this.$table.find("thead"),
        this.settings = t.extend({}, t.tablesort.defaults, s),
        this.$sortCells = this.$thead.length > 0 ? this.$thead.find("th:not(.no-sort)") : this.$table.find("th:not(.no-sort)"),
        this.$sortCells.on("click.tablesort", function() {
            i.sort(t(this))
        }),
        this.index = null,
        this.$th = null,
        this.direction = null
    }
    ,
    t.tablesort.prototype = {
        sort: function(e, s) {
            var i = new Date
              , n = this
              , o = this.$table
              , l = o.find("tbody").length > 0 ? o.find("tbody") : o
              , a = l.find("tr").has("td, th")
              , r = a.find(":nth-child(" + (e.index() + 1) + ")").filter("td, th")
              , d = e.data().sortBy
              , h = []
              , c = r.map(function(s, i) {
                return d ? "function" == typeof d ? d(t(e), t(i), n) : d : null != t(this).data().sortValue ? t(this).data().sortValue : t(this).text()
            });
            0 !== c.length && (this.index !== e.index() ? (this.direction = "asc",
            this.index = e.index()) : "asc" !== s && "desc" !== s ? this.direction = "asc" === this.direction ? "desc" : "asc" : this.direction = s,
            s = "asc" == this.direction ? 1 : -1,
            n.$table.trigger("tablesort:start", [n]),
            n.log("Sorting by " + this.index + " " + this.direction),
            n.$table.css("display"),
            setTimeout(function() {
                n.$sortCells.removeClass(n.settings.asc + " " + n.settings.desc);
                for (var o = 0, d = c.length; o < d; o++)
                    h.push({
                        index: o,
                        cell: r[o],
                        row: a[o],
                        value: c[o]
                    });
                h.sort(function(t, e) {
                    return n.settings.compare(t.value, e.value) * s
                }),
                t.each(h, function(t, e) {
                    l.append(e.row)
                }),
                e.addClass(n.settings[n.direction]),
                n.log("Sort finished in " + ((new Date).getTime() - i.getTime()) + "ms"),
                n.$table.trigger("tablesort:complete", [n]),
                n.$table.css("display")
            }, c.length > 2e3 ? 200 : 10))
        },
        log: function(e) {
            (t.tablesort.DEBUG || this.settings.debug) && console && console.log && console.log("[tablesort] " + e)
        },
        destroy: function() {
            return this.$sortCells.off("click.tablesort"),
            this.$table.data("tablesort", null),
            null
        }
    },
    t.tablesort.DEBUG = !1,
    t.tablesort.defaults = {
        debug: t.tablesort.DEBUG,
        asc: "sorted ascending",
        desc: "sorted descending",
        compare: function(t, e) {
            return t > e ? 1 : t < e ? -1 : 0
        }
    },
    t.fn.tablesort = function(e) {
        var s, i;
        return this.each(function() {
            s = t(this),
            i = s.data("tablesort"),
            i && i.destroy(),
            s.data("tablesort", new t.tablesort(s,e))
        })
    }
}(window.Zepto || window.jQuery);
